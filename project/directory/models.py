import os
import uuid
from django.db import models
from project.accounts.models import User


class Tag(models.Model):

    class Meta:
        verbose_name_plural = "Tags"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


def upload_to(instance, filename):
    """Return a unique path for the cover upload"""
    random_string = uuid.uuid4().hex
    filename = "%s-%s" % (random_string, filename)
    return os.path.join(Entry.UPLOAD_PATH, filename)


class Entry(models.Model):

    class Meta:
        verbose_name_plural = "Entries"

    UPLOAD_PATH = 'covers'
    MAX_LOGO_WIDTH = 500
    MAX_LOGO_HEIGHT = 500

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, unique=True)
    short_description = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name="entries")
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)

    cover = models.ImageField(upload_to=upload_to, null=True, blank=True)
    website_url = models.URLField()
    repo_url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    is_approved = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def _get_cover_link(self, url):
        if not url:
            return None

        return u'<img width="80px" src="%s" />' % (url.url)

    def thumbnail_cover(self):
        return self._get_cover_link(self.cover)
    thumbnail_cover.short_description = 'Cover Thumbnail'
    thumbnail_cover.allow_tags = True
