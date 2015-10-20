import requests
from django.conf import settings
from django.http import Http404
from django.views.generic import View


class OAuthCallbackView(View):

    def get(self, request):
        code = request.GET.get('code', '')
        response = requests.post("https://github.com/login/oauth/access_token", headers={"Accept": "application/json"}, data={
            "client_id": settings.GITHUB_CLIENT_ID,
            "client_secret": settings.GITHUB_CLIENT_SECRET,
            "code": code
        })

        if response.status_code != 200:
            raise Http404("Oops! Something went wrong!")

        payload = response.json()

        response_user = requests.get("https://api.github.com/user", headers={
            "Authorization": ("token %s" % payload['access_token'])
        })

        if response_user.status_code != 200:
            raise Http404("Oops! Something went wrong!")

        import json
        print(json.dumps(response_user.json(), indent=4, sort_keys=True))
