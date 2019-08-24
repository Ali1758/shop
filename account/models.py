from django.db import models
from django.contrib.auth.models import AbstractUser


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        default_related_name = 'city'
        verbose_name = 'city'
        verbose_name_plural = 'cities'
        db_table = 'user_city'

    def __str__(self):
        return '{}'.format(self.name)


class Zone(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='zones')
    name = models.CharField(max_length=5)


class Sector(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    zone = models.ForeignKey(city.zones, on_delete=models.CASCADE)


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=255)

    class Meta:
        unique_together = (('username', 'address'),)
