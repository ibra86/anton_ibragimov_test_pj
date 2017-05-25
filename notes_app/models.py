from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['pk']

    def delete(self):
        # book to keep
        bk_keep = BookContent.objects.exclude(
            note_id__in=[self.id]).values_list('book_id', flat=True)
        # others - to delete
        Book.objects.exclude(id__in=list(bk_keep)).delete()
        return super(Note, self).delete()

    def __unicode__(self):
        return self.title


class Book(models.Model):

    title = models.CharField(max_length=200)
    note = models.ManyToManyField(
        Note,
        through='BookContent',
    )

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title


class BookContent(models.Model):
    note = models.ForeignKey(
        Note, related_name='book_content', on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, related_name='book_content', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('note', 'book')

    def __unicode__(self):
        return 'Note "%s" of Book "%s"' % (self.note, self.book)


class RequestStat(models.Model):
    line = models.TextField()
    time = models.DateTimeField()
    is_new = models.NullBooleanField(null=True)

    def __unicode__(self):
        return str(self.id) + " -- " + self.line + " -- "\
            + str(self.time.strftime("%Y-%m-%d %H:%M:%S")) + " -- "\
            + "is_new: " + str(self.is_new)
