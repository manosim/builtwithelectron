from django.conf import settings
from django.views.generic import TemplateView


class RobotsView(TemplateView):

    content_type = 'text/plain'

    def get_template_names(self):

        if settings.DEBUG:
            return "staging-robots.txt"
        else:
            return "production-robots.txt"
