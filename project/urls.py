"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from project.common.views import RobotsView

api_urls = [
    url(r'^directory/', view=include('project.directory.urls_api', namespace='directory')),
]

urlpatterns = [

    url('api/', include(api_urls, namespace='api')),

    url(r'^', view=include('project.directory.urls', namespace='directory')),
    url(r'^accounts/', view=include('project.accounts.urls', namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),

    # Robots
    url(regex=r'^robots.txt$', view=RobotsView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
