from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE)

