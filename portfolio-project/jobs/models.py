from django.db import models

class job(models.Model):
    image = models.ImageField(upload_to='image/')
    summary = models.CharField(max_length=200)
