from __future__ import unicode_literals

import datetime

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.db import models
from django.template import Context, loader
from django.utils.translation import ugettext as _


# Create your models here.
class EmailValidationManager(models.Manager):
    """
    Email validation manager
    """

    def verify(self, key):
        try:
            verify = self.get(key=key)
            if not verify.is_expired():
                verify.user.email = verify.email
                verify.user.save()
                verify.delete()
                return True
            else:
                verify.delete()
                return False
        except:
            return False

    def getuser(self, key):
        try:
            return self.get(key=key).user
        except:
            return False

    def add(self, user, email):
        """
        Add a new validation process entry
        """
        while True:
            key = User.objects.make_random_password(70)
            try:
                EmailValidation.objects.get(key=key)
            except EmailValidation.DoesNotExist:
                self.key = key
                break
        template_body = "userprofile/email/validation.txt"
        template_subject = "userprofile/email/validation_subject.txt"
        site_name, domain = Site.objects.get_current(
        ).name, Site.objects.get_current().domain
        body = loader.get_template(template_body).render(Context(locals()))
        subject = loader.get_template(template_subject).render(
            Context(locals())).strip()
        send_mail(
            subject=subject,
            message=body,
            from_email=None,
            recipient_list=[email])
        user = User.objects.get(username=str(user))
        self.filter(user=user).delete()
        return self.create(user=user, key=key, email=email)


class EmailValidation(models.Model):
    """
    Email Validation model
    """
    user = models.ForeignKey(User, unique=True)
    email = models.EmailField(blank=True)
    key = models.CharField(max_length=70, unique=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    objects = EmailValidationManager()

    def __unicode__(self):
        return _("Email validation process for %(user)s") % {'user': self.user}

    def is_expired(self):
        return (datetime.datetime.today() - self.created).days > 0

    def resend(self):
        """
        Resend validation email
        """
        template_body = "userprofile/email/validation.txt"
        template_subject = "userprofile/email/validation_subject.txt"
        site_name, domain = Site.objects.get_current(
        ).name, Site.objects.get_current().domain
        key = self.key
        body = loader.get_template(template_body).render(Context(locals()))
        subject = loader.get_template(template_subject).render(
            Context(locals())).strip()
        send_mail(
            subject=subject,
            message=body,
            from_email=None,
            recipient_list=[self.email])
        self.created = datetime.datetime.now()
        self.save()
        return True
