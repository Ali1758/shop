from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE)


class Products(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField()
    off_percent = models.DecimalField(max_digits=4, decimal_places=2)
    off_expire = models.DateField()
    price = models.PositiveIntegerField(max_length=10)
    count = models.PositiveIntegerField(max_length=5)
    sold = models.PositiveIntegerField(max_length=5)
    rate = models.PositiveIntegerField(max_length=1)
    rate_count = models.PositiveIntegerField(max_length=5)
    fast_send = models.BooleanField(default=False)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
