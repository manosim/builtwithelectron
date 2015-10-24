from django.conf.urls import patterns, url
from project.directory.views import HomePageView, SubmitEntryView

urlpatterns = patterns('',

    url(r'^$', HomePageView.as_view(), name="home"),
    url(r'^submit/$', SubmitEntryView.as_view(), name="submit"),

)
