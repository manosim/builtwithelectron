from django import template
from project.accounts.helpers import get_oauth_url

register = template.Library()


@register.inclusion_tag('common/menu.html', takes_context=True)
def menu(context):
    user = context['request'].user
    OAUTH_URL = get_oauth_url()

    return {
        'user': user,
        'OAUTH_URL': OAUTH_URL
    }
