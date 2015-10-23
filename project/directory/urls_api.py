from django.conf.urls import patterns, url
from project.directory.views_api import SubmitEntryView


urlpatterns = patterns('',

    url(r'^submit/$',
        view=SubmitEntryView.as_view(), name="submit"),

)
