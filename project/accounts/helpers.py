from django.conf import settings


def get_oauth_url():
    """
    Generates the oAuth url for authentication with GitHub
    """

    client_id = settings.GITHUB_CLIENT_ID
    oauth_url = ("https://github.com/login/oauth/authorize?client_id"
        "=%s&scope=user:email" % (client_id))
    return oauth_url
