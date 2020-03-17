from django.db import models
from django.urls import reverse
# Models

class Podcast(models.Model):
    url = models.URLField(max_length=200, unique=True)
    title = models.CharField(max_length=100, unique=False)
    created_at = models.DateTimeField(auto_now=True)
    rj_name = models.CharField(max_length=200)
    description = models.TextField(max_length=1024, blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('podcast:detail', kwargs={'pk':self.pk})

class LiveShow(models.Model):
    url = models.URLField(max_length=200, unique=True)
    title = models.CharField(max_length=100, unique=False)
    date = models.DateTimeField(auto_now=True)
    rj_name = models.CharField(max_length=200)
    
    def __str__(self):
        return  str(self.title) + " - " + str(self.date)
