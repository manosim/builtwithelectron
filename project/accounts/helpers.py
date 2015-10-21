from django.conf import settings


def get_oauth_url():
    """
    Generates the oAuth url for authentication with GitHub
    """

    client_id = settings.GITHUB_CLIENT_ID
    redirect_uri = settings.GITHUB_REDIRECT_URI
    oauth_url = ("https://github.com/login/oauth/authorize?client_id"
        "=%s&scope=user:email&redirect_uri=%s" % (client_id, redirect_uri))
    return oauth_url
