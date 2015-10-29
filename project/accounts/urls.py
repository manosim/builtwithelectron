from django.conf.urls import patterns, url
from project.accounts.views import OAuthCallbackView, ProfileView

urlpatterns = patterns('',

    url(r'^oauth-callback/$', OAuthCallbackView.as_view(), name="oauth-callback"),
    url(r'^profile/$', ProfileView.as_view(), name="profile"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'directory:home'}, name='logout'),

)
