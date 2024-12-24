from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


class EmailService:
    def send_activation_email(self, username, domain, uid, to_email, token):
        subject = 'Activate your account'
        message = render_to_string('registration/activation_email.html', {
            'username': username,
            'domain': domain,
            'uid': uid,
            'token': token,
        })

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [to_email],
            fail_silently=False,
        )
