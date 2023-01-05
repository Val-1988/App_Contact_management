from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name, self.second_name, self.patronymic
