from django import template
from project.directory.models import Entry
register = template.Library()


@register.inclusion_tag('directory/featured.html')
def featured():

    featured = Entry.objects.filter(is_approved=True, is_featured=True).last()

    return {'featured': featured}
