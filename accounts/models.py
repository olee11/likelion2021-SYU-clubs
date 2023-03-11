from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email = email,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username = username,
            email = email,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    objects = UserManager()

    def __str__(self):
        return self.club_name
