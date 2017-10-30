from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    img_profile = models.ImageField('프로필 이미지', upload_to='user', blank=True)
