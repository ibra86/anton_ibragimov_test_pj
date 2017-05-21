from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title