# Create your models here.
"""
Model configuration for Aku authentication
"""

import os.path

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

AVATAR_SIZES = (128, 96, 64, 48, 32, 24, 16)


class Avatar(models.Model):
    """
    Avatar model
    """
    image = models.ImageField(upload_to="avatars/%Y/%b/%d")
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    valid = models.BooleanField()

    class Meta:
        unique_together = (('user', 'valid'), )

    def __unicode__(self):
        return _("%s's Avatar") % self.user

    def delete(self):
        base, filename = os.path.split(self.image.path)
        name, extension = os.path.splitext(filename)
        try:
            for key in AVATAR_SIZES:
                path = os.path.join(base, "%s.%s%s" % (name, key, extension))
                if os.path.isfile(path):
                    os.remove(path)
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        except:
            pass
        super(Avatar, self).delete()

    def save(self):
        for avatar in Avatar.objects.filter(
                user=self.user, valid=self.valid).exclude(id=self.id):
            base, filename = os.path.split(avatar.image.path)
            name, extension = os.path.splitext(filename)
            for key in AVATAR_SIZES:
                try:
                    os.remove(
                        os.path.join(base, "%s.%s%s" % (name, key, extension)))
                except:
                    pass
            avatar.delete()
        super(Avatar, self).save()
