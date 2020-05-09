from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name


