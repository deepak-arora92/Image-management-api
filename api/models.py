from __future__ import unicode_literals

from django.db import models
import os
def user_directory_path(instance,filename):
    return os.path.join(instance.path,filename)

def images_only(value):
    from django.core.exceptions import ValidationError
    if not value.content_type.startswith('image'):
        raise ValidationError(u'Unsupported file extension.')

class Document(models.Model):
    def __unicode__(self):
        return '%s' % (self.image.name)
    path = models.CharField(default='',max_length=100)
    image = models.FileField(upload_to=user_directory_path,validators=[images_only])
