from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from project.directory.models import Entry, Tag


class HasCoverFilter(admin.SimpleListFilter):
    title = _('Has Cover')
    parameter_name = 'cover'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Yes'),
            ('0', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(cover='')
        elif self.value() == '1':
            return queryset.exclude(cover='')
        return queryset


class IsApprovedFilter(admin.SimpleListFilter):
    title = _('Is Approved')
    parameter_name = 'approved'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Yes'),
            ('0', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(is_approved=False)
        elif self.value() == '1':
            return queryset.filter(is_approved=True)
        return queryset


class IsFeaturedFilter(admin.SimpleListFilter):
    title = _('Is Featured')
    parameter_name = 'featured'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Yes'),
            ('0', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(is_featured=False)
        elif self.value() == '1':
            return queryset.filter(is_featured=True)
        return queryset


class EntriesAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_cover', 'name', 'short_description', 'author', 'get_tags', 'website_url', 'repo_url', 'has_description',)
    # list_display = ('name', 'thumbnail_cover', 'short_description', 'author', 'get_tags', 'website_url', 'repo_url', 'has_description',)
    list_filter = (IsApprovedFilter, HasCoverFilter, IsFeaturedFilter,)

    fieldsets = (
        ('Required Information', {'fields': ('name', 'short_description', 'author', 'website_url', 'is_approved', 'is_featured', )}),
        ('Additional Information', {'fields': ('cover', 'thumbnail_cover', 'tags', 'repo_url', 'description',)}),
    )

    readonly_fields = ('thumbnail_cover',)
    search_fields = ('name', 'short_description', 'website_url', 'repo_url',)

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
