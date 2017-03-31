# Create your models here.

import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext as _

from .avatar import Avatar
from .countries import CountryField

GENDER_CHOICES = (
    ('F', _('Female')),
    ('M', _('Male')), )
PROVINCE_CHOICES = (
    ('Aceh, D.I.', 'Aceh, D.I.'),
    ('Bali', 'Bali'),
    ('Bangka Belitung', 'Bangka Belitung'),
    ('Banten', 'Banten'),
    ('Bengkulu', 'Bengkulu'),
    ('Gorontalo', 'Gorontalo'),
    ('Jakarta', 'Jakarta, DKI'),
    ('Jambi', 'Jambi'),
    ('Jawa Barat', 'Jawa Barat'),
    ('Jawa Tengah', 'Jawa Tengah'),
    ('Jawa Timur', 'Jawa Timur'),
    ('Kalimantan Barat', 'Kalimantan Barat'),
    ('Kalimantan Selatan', 'Kalimantan Selatan'),
    ('Kalimantan Tengah', 'Kalimantan Tengah'),
    ('Kalimantan Timur', 'Kalimantan Timur'),
    ('Lampung', 'Lampung'),
    ('Maluku', 'Maluku'),
    ('Maluku Utara', 'Maluku Utara'),
    ('Nusa Tenggara Barat', 'Nusa Tenggara Barat'),
    ('Nusa Tenggara Timur', 'Nusa Tenggara Timur'),
    ('Papua Barat', 'Papua Barat'),
    ('Papua Tengah', 'Papua Tengah'),
    ('Papua Timur', 'Papua Timur'),
    ('Riau', 'Riau'),
    ('Sulawesi Selatan', 'Sulawesi Selatan'),
    ('Sulawesi Tengah', 'Sulawesi Tengah'),
    ('Sulawesi Tenggara', 'Sulawesi Tenggara'),
    ('Sulawesi Utara', 'Sulawesi Utara'),
    ('Sumatra Barat', 'Sumatra Barat'),
    ('Sumatra Selatan', 'Sumatra Selatan'),
    ('Sumatra Utara', 'Sumatra Utara'),
    ('Yogyakarta', 'Yogyakarta, D.I.'), )
OCCUPATION_CHOICES = (
    ('1', _('Student/College')),
    ('2', _('Civil Servants')),
    ('3', _('Private Employees')),
    ('4', _('Entrepreneur')), )

SINCE_CHOICES = (
    ('2005', '2005'),
    ('2006', '2006'),
    ('2007', '2007'),
    ('2008', '2008'),
    ('2009', '2009'),
    ('2010', '2010'),
    ('2011', '2011'), )

STATUS_CHOICES = (
    ('Y', _('Yes')),
    ('N', _('No')), )


class BaseProfile(models.Model):
    """
    User profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    country = CountryField(null=True, blank=True, default='ID')
    latitude = models.DecimalField(
        max_digits=10, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=10, decimal_places=6, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    status = models.CharField(
        _('join survey?'), max_length=1, choices=STATUS_CHOICES, default='N')

    class Meta:
        abstract = True

    def has_avatar(self):
        return Avatar.objects.filter(user=self.user, valid=True).count()

    def __unicode__(self):
        return _("%s's profile") % self.user

    def get_absolute_url(self):
        return reverse("profile_public", args=[self.user])


class Profile(BaseProfile):
    firstname = models.CharField(
        _('firstname'), max_length=255, blank=False, null=False)
    surname = models.CharField(
        _('lastname'), max_length=255, blank=False, null=False)
    gender = models.CharField(
        _('gender'),
        max_length=1,
        choices=GENDER_CHOICES,
        blank=False,
        null=False)
    birthdate = models.DateField(
        _('birthdate'), default=datetime.date.today, blank=False, null=False)
    address = models.TextField(_('address'), blank=False, null=False)
    city = models.CharField(_('city'), max_length=255, blank=False, null=False)
    province = models.CharField(
        _('province'),
        max_length=255,
        choices=PROVINCE_CHOICES,
        blank=False,
        null=False)
    occupation = models.CharField(
        _('occupation'),
        max_length=255,
        choices=OCCUPATION_CHOICES,
        blank=False,
        null=False)
    since = models.CharField(
        _('use BlankOn since'),
        max_length=4,
        choices=SINCE_CHOICES,
        blank=False,
        null=False)
    url = models.URLField(_('personal website'), blank=True, null=True)
    about = models.TextField(_('about me'), blank=True, null=True)


class SSHKeys(models.Model):
    user = models.ForeignKey(User, verbose_name=_('user'))
    fingerprint = models.CharField(
        _('fingerprint'), max_length=48, unique=True)
    key = models.TextField(verbose_name=_('key'))

    def __unicode__(self):
        return "SSH Keys for user %s" % self.user
