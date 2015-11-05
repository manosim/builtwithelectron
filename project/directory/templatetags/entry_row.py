from django import template


register = template.Library()


@register.inclusion_tag('directory/entry-row.html', takes_context=True)
def entry_row(context, entry):
    return {
        'entry': entry,
        'MEDIA_URL': context['MEDIA_URL']
    }
