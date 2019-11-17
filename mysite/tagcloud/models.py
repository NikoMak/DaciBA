from django.db import models
from django.contrib.auth.models import User

import datetime

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    created_on = models.DateTimeField(null=False, default=datetime.datetime.now())

    def __str__(self):
        return f"{self.user}: {self.tag}"


class Topic(models.Model):
    topic = models.CharField(max_length=32)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.topic} (" + ", ".join(str(tag) for tag in self.tag.all()) + ")"


class Project(models.Model):
    project = models.CharField(max_length=32)
    topic = models.ManyToManyField(Topic, blank=True)

    def __str__(self):
        return f"{self.project} [" + ", ".join(str(topic) for topic in self.topic.all()) + "]"

