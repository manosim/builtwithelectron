from django.contrib import admin
from project.directory.models import Entry, Tag


class EntriesAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_cover', 'name', 'short_description', 'author', 'get_tags', 'website_url', 'repo_url', 'has_description',)

    fieldsets = (
        ('Required Information', {'fields': ('name', 'short_description', 'author', 'website_url', )}),
        ('Additional Information', {'fields': ('cover', 'thumbnail_cover', 'tags', 'repo_url', 'description',)}),
    )

    readonly_fields = ('thumbnail_cover',)

    def get_tags(self, obj):
        return "\n".join([p.name for p in obj.tags.all()])
    get_tags.short_description = 'Tags'

    def has_description(self, obj):
        return obj.description != ""
    has_description.short_description = 'Desc.'
    has_description.boolean = True


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_no_apps', 'created', 'modified',)

    def get_no_apps(self, obj):
        return Entry.objects.filter(tags=obj).count()
    get_no_apps.short_description = 'No. of Apps'

admin.site.register(Entry, EntriesAdmin)
admin.site.register(Tag, TagsAdmin)
