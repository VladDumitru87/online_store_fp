from django.db import models


class User(models.Model):
    login = models.CharField(max_length=8, unique=True)
    password = models.CharField(max_length=12)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    phone_number = models.BigIntegerField(unique=True)
    id_code = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    dt_entrance = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.id_code)

