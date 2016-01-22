import uuid
from cloudinary.models import CloudinaryField
from django.db import models
from django.utils.text import slugify
from django_dbq.models import Job
from project.accounts.models import User


class Tag(models.Model):

    class Meta:
        verbose_name_plural = "Tags"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Entry(models.Model):

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Entries"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name="entries")
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)

    cover = CloudinaryField(null=True, blank=True)
    website_url = models.URLField(null=True, blank=True)
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
        workspace = {
            "subject": "Your submission to Built with Electron got approved.",
            "recipient_list": [self.author.email],
            "mail_params": {
                'username': self.author.username,
                'entry_name': self.name,
                'entry_slug': self.slug
            },
            "plain_template": "emails/submission_approval.txt",
            "html_template": "emails/submission_approval.html"
        }

        Job.objects.create(name='send_email', workspace=workspace)

    def send_admins_new_entry_email(self):
        """ Notify admins that a new submission awaits approval """
        admins = User.objects.filter(is_active=True, is_admin=True)
        admins_emails = [user.email for user in admins]

        workspace = {
            "subject": "There is a new submission at Built with Electron.",
            "recipient_list": admins_emails,
            "mail_params": {
                'entry_name': self.name
            },
            "plain_template": "emails/admin_new_submission.txt",
            "html_template": "emails/admin_new_submission.html"
        }

        Job.objects.create(name='send_email', workspace=workspace)

    def save(self, *args, **kwargs):
        """ If `is_approved` changed and is True, email the user """
        try:
            prev_state = Entry.objects.get(id=self.id).is_approved
            new_state = self.is_approved

            if (prev_state != new_state) and new_state:
                self.send_user_approval_email()

        except self.DoesNotExist:
            pass

        # Auto-populate the slugfield
        if not self.slug:
            self.slug = slugify(self.name)

        super(Entry, self).save(*args, **kwargs)
