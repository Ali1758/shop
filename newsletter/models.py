from django.db import models


class Newsletter(models.Model):
    name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
