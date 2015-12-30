import logging
from django.conf import settings
from django.core.mail import send_mail as django_send_mail
from django.template.loader import render_to_string


logger = logging.getLogger(__name__)


def send_email(job):
    logger.info("Sending email with subject %s to %s", job.workspace['subject'], ", ".join(job.workspace['recipient_list']))

    job.workspace['mail_params']['site_url'] = settings.SITE_URL

    msg_plain = render_to_string(job.workspace['plain_template'], job.workspace['mail_params'])
    msg_html = render_to_string(job.workspace['html_template'], job.workspace['mail_params'])

    django_send_mail(
        subject=job.workspace['subject'],
        message=msg_plain,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=job.workspace['recipient_list'],
        html_message=msg_html,
    )
