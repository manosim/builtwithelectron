from django.contrib import admin
from project.directory.models import Entry, Tag


class EntriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'author', 'get_tags', 'cover', 'website_url', 'repo_url', 'description',)

    def get_tags(self, obj):
        return "\n".join([p.name for p in obj.tags.all()])


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Entry, EntriesAdmin)
admin.site.register(Tag, TagsAdmin)
