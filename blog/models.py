from cgitb import text
from re import T
from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Post(models.Model):
  author = models.CharField('Author', max_length=150)
  title = models.CharField('Title', max_length=200)
  text = models.TextField('Text')
  created_date = models.DateTimeField('Created date', default=timezone.now)
  publish_date = models.DateTimeField('Publish date', null=True, blank=True)

  def publish(self):
    self.publish_date = timezone.now
    self.save()

  def __str__(self):
    return self.title


