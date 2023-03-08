from django.db import models

class User(models.Model):
    club_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.club_name
