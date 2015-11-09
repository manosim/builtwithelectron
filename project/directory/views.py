from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
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
        print()
        print()
        print("GET")
        print()
        print()
        self.object_list = self.get_queryset()
        # allow_empty = self.get_allow_empty()
        # if not allow_empty and len(self.object_list) == 0:
        #     raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
        #                   % {'class_name': self.__class__.__name__})
        # self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object_list=self.object_list, form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        if not request.POST.get('keywords'):
            return HttpResponseRedirect(reverse('directory:home'))

        self.queryset = self.get_queryset()
        print()
        # form_class = self.get_form_class()
        # form = self.get_form(form_class)
        return super(SearchResultsView, self).get(request, *args, **kwargs)
        # context = self.get_context_data(object_list=self.object_list, form=form)
        # # return self.render_to_response(context)
        # self.object_list = self.get_queryset()
        # return self.render_to_response(self.get_context_data(object_list=self.object_list, form=form))

    def get_success_url(self):
        pass
        # return reverse('author-detail', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        keywords = self.request.POST.get('keywords')
        results = Entry.objects.filter(slug=keywords)  # FIXME: Get only approved entries
        results = Entry.objects.all()  # FIXME: Get only approved entries
        return results

    # def get_context_data(self, **kwargs):
    #     context = super(SearchResultsView, self).get_context_data(**kwargs)
    #     return context

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super(SearchResultsView, self).form_valid(form)
