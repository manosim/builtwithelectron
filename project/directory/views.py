from django.core import serializers
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from project.accounts.helpers import get_oauth_url
from project.directory.models import Entry, Tag


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        latest = Entry.objects.all()[:5]  # FIXME: Get only approved entries
        # latest = Entry.objects.filter(is_approved=True, is_featured=False)[:5]

        context = super(HomePageView, self).get_context_data(**kwargs)
        context['OAUTH_URL'] = get_oauth_url()
        context['latest'] = latest
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


class EntryDetailView(DetailView):

    model = Entry
    template_name = "directory/detail.html"

    def get_context_data(self, **kwargs):
            context = super(EntryDetailView, self).get_context_data(**kwargs)
            # context['now'] = timezone.now()
            return context
