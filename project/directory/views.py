from django.core import serializers
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from project.accounts.helpers import get_oauth_url
from project.directory.models import Entry, Tag
from project.directory.forms import SearchForm


class HomePageView(ListView):

    model = Entry
    template_name = "home.html"
    paginate_by = 10

    def get_queryset(self):
        latest = Entry.objects.all().order_by('-created')  # FIXME: Get only approved entries
        # latest = Entry.objects.filter(is_approved=True, is_featured=False)
        return latest

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['is_homepage'] = True
        context['OAUTH_URL'] = get_oauth_url()
        return context


class SubmitEntryView(TemplateView):

    template_name = "directory/submit.html"

    def get_context_data(self, **kwargs):
        tags = Tag.objects.all()
        tags_json = serializers.serialize('json', tags)

        context = super(SubmitEntryView, self).get_context_data(**kwargs)
        context['OAUTH_URL'] = get_oauth_url()
        context['tags'] = tags_json
        return context


class EntryDetailView(FormMixin, DetailView):

    model = Entry
    slug_field = 'slug'
    template_name = "directory/detail.html"

    def get_context_data(self, **kwargs):
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context


class TagEntriesListView(ListView):

    model = Entry
    template_name = "directory/tag-entries.html"
    paginate_by = 10

    def get_queryset(self):
        slug = self.kwargs['slug']
        queryset = Entry.objects.filter(tags__name=slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TagEntriesListView, self).get_context_data(**kwargs)
        context['tag_name'] = self.kwargs['slug']
        return context


class SearchResultsView(FormMixin, ListView):

    model = Entry
    template_name = "directory/search-results.html"
    form_class = SearchForm
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        return super(SearchResultsView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        keywords = self.request.POST.get('keywords')
        if keywords:
            return Entry.objects.filter(
                Q(name__icontains=keywords) | Q(short_description__icontains=keywords) |
                Q(author__username__icontains=keywords) | Q(description__icontains=keywords)
            ).exclude(is_approved=False)
        return []

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)

        object_list = context['object_list']

        if object_list:
            context['found'] = True
        else:
            context['found'] = False
            context['object_list'] = Entry.objects.filter(is_approved=True)

        context['keywords'] = self.request.POST.get('keywords')
        return context
