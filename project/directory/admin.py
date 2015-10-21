from django.contrib import admin
from project.directory.models import Entry, Tag


class EntriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'author', 'get_tags', 'cover', 'website_url', 'repo_url', 'description',)

    fieldsets = (
        (None, {'fields': ('name', 'short_description',)}),
        ('Personal info', {'fields': ('author',)}),
        ('Permissions', {'fields': ('thumbnail_cover', 'website_url', 'repo_url', 'description',)}),
    )

    readonly_fields = ('thumbnail_cover',)

    def get_tags(self, obj):
        return "\n".join([p.name for p in obj.tags.all()])


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Entry, EntriesAdmin)
admin.site.register(Tag, TagsAdmin)
