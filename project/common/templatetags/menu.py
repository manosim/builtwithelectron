from django import template
from project.accounts.helpers import get_oauth_url
from project.directory.forms import SearchForm

register = template.Library()


@register.inclusion_tag('common/menu.html', takes_context=True)
def menu(context):
    if context['request'].method == 'GET':
        user = context['request'].user
        OAUTH_URL = get_oauth_url()
        form = SearchForm()

        return {
            'user': user,
            'form': form,
            'OAUTH_URL': OAUTH_URL
        }
    else:
        user = context['request'].user
        OAUTH_URL = get_oauth_url()

        return {
            'user': user,
            'OAUTH_URL': OAUTH_URL
        }
