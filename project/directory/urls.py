from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from project.directory.views import HomePageView, SubmitEntryView

urlpatterns = patterns('',

    url(r'^$', HomePageView.as_view(), name="home"),
    url(r'^submit/$', SubmitEntryView.as_view(), name="submit"),

)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
