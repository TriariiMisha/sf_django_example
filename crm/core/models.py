from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_joined = None
