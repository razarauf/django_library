from __future__ import unicode_literals
from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.name

class Book(models.Model):
  library = models.ForeignKey(Library)
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200, blank=True)
  timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated = models.DateTimeField(auto_now_add=False, auto_now=True)

  def __unicode__(self):
        return self.title

class BookTags(models.Model):
    tag = models.ForeignKey(Book)
    tagname = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.tagname
