import requests
from django.conf import settings
from django.contrib.auth import login
from django.http import Http404
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from project.accounts.models import User


class OAuthCallbackView(RedirectView):

    pattern_name = 'directory:home'
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        code = self.request.GET.get('code', '')

        if not code:
            raise Http404("Oops! We could not authenticate you with GitHub. Looks like you did not authorize the app.")

        response = requests.post("https://github.com/login/oauth/access_token", headers={"Accept": "application/json"}, data={
            "client_id": settings.GITHUB_CLIENT_ID,
            "client_secret": settings.GITHUB_CLIENT_SECRET,
            "code": code
        })

        if response.status_code != 200:
            raise Http404("Oops! We counld not authenticate you with GitHub.")

        payload = response.json()

        response_user = requests.get("https://api.github.com/user", headers={
            "Authorization": ("token %s" % payload['access_token'])
        })

        response_emails = requests.get("https://api.github.com/user/emails", headers={
            "Authorization": ("token %s" % payload['access_token'])
        })

        if response_user.status_code != 200 or response_emails.status_code != 200:
            raise Http404("Oops! We couldn't get your details!")

        payload_user = response_user.json()
        payload_emails = response_emails.json()

        for email in payload_emails:
            if email['primary'] and email['verified']:
                username = payload_user['login']
                avatar_url = payload_user['avatar_url']
                email_address = email['email']

        if not username or not email_address or not avatar_url:
            raise Http404("Oops! We couldn't get your details!")

        # Now get or create the user
        user, created = User.objects.get_or_create(username=username,
            defaults={'email': email_address, 'avatar_url': avatar_url})

        # Okay, login the user
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
        login(self.request, user)

        # Finally redirect the user to the homepage view
        return super(OAuthCallbackView, self).get_redirect_url(*args, **kwargs)


class ProfileView(DetailView):

    template_name = "accounts/profile.html"

    def get_object(self, queryset=None):
        return get_object_or_404(User, username=self.request.user.username)

    def get_context_data(self, **kwargs):
        entries = self.request.user.entries.filter(is_approved=True)
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['entries'] = entries
        context['entries_total'] = entries.count()
        return context
