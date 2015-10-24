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

    def send_user_approval_email(self):
        """ Notify the user that the submission got approved """
        # send_mail(
        #     'email/admin_notification_user_approval.tpl',
        #     {
        #         'user': self,
        #         'site_url': settings.SITE_URL
        #     }, settings.DEFAULT_FROM_EMAIL, settings.ADMIN_EMAILS
        # )

    def save(self, *args, **kwargs):
        """ If `is_approved` changed and is True, email the user """
        try:
            prev_state = Entry.objects.get(id=self.id).is_approved
            new_state = self.is_approved

            if (prev_state != new_state) and new_state:
                self.send_user_approval_email()

        except self.DoesNotExist:
            pass

        super(Entry, self).save(*args, **kwargs)
