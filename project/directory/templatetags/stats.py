from django import template
from project.directory.models import Entry, Tag
register = template.Library()


@register.inclusion_tag('directory/stats.html')
def stats():

    entries_count = Entry.objects.filter(is_approved=True).count()
    tags_count = Tag.objects.all().count()

    return {'entries_count': entries_count, 'tags_count': tags_count}
