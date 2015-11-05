from django import template
from project.directory.models import Entry
register = template.Library()


@register.inclusion_tag('directory/featured.html', takes_context=True)
def featured(context):

    featured = Entry.objects.filter(is_approved=True, is_featured=True).last()
    return {
        'featured': featured,
        'MEDIA_URL': context['MEDIA_URL']
    }
