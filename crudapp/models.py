from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(default=False)

# login hisseni html-den chixartmaq
# email send funksiyasi
# reng top rate sorting asc desc
# produkta bir chox shekiller chixartmaq
# django jasmin istifade edib admin paneli duzeltmek

class PostModel(models.Model):
    #User = get_user_model()
    title = models.CharField(max_length=20, null=True, blank=True)
    subtitle = models.CharField(max_length=40, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now=True)
    headimage = models.ImageField(upload_to='post_images', null=True, blank=True)

    def __str__(self):
        return f'{self.title}/{self.subtitle}'




