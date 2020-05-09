from django.db import models
from django.utils import timezone


class PostAdd(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to="media/images/%y%m%d_%h%m", null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
