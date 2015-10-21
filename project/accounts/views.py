import requests
from django.conf import settings
from django.contrib.auth import login
from django.http import Http404
from django.views.generic.base import RedirectView
from project.accounts.models import User


class OAuthCallbackView(RedirectView):

    pattern_name = 'directory:home'

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
                email_address = email['email']

        if not username or not email_address:
            raise Http404("Oops! We couldn't get your details!")

        # Now get or create the user
        user, created = User.objects.get_or_create(username=username,
            defaults={'email': email_address})

        # Okay, login the user
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
        login(self.request, user)

        # Finally redirect the user to the homepage view
        return super(OAuthCallbackView, self).get_redirect_url(*args, **kwargs)
