from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from .util import translit_to_eng


class Poster(models.Model):
    title = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True)
    price = models.IntegerField()
    short_description = models.TextField(blank=True, null=True)
    full_description = models.TextField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_event = models.DateTimeField()
    preview_image = models.CharField(max_length=255, null=True, blank=True)
    background_image = models.CharField(max_length=255, null=True, blank=True)
    subscribers = models.ManyToManyField('User', related_name='user')

    def __str__(self):
        return f'{self.creator}_{self.title}'

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def save(self, *args, **kwargs):
        self.slug = translit_to_eng(slugify(self.title, allow_unicode=True))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('poster', kwargs={'post_slug': self.slug})


class User(models.Model):
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    nickname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    about = models.TextField(blank=True, null=True)
    hobby = models.TextField(blank=True, null=True)
    is_creator = models.BooleanField(default=False)
    created_events = models.ManyToManyField('Poster', related_name='poster')

    def __str__(self):
        return self.nickname


class Application(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey('User', related_name='sender', on_delete=models.PROTECT)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    call_time = models.DateTimeField()
