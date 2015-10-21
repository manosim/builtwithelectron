from django.conf import settings
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['CLIENT_ID'] = settings.GITHUB_CLIENT_ID
        context['REDIRECT_URI'] = settings.GITHUB_REDIRECT_URI
        return context


class SubmitEntryView(TemplateView):

    template_name = "submit.html"

    def get_context_data(self, **kwargs):
        context = super(SubmitEntryView, self).get_context_data(**kwargs)
        return context
