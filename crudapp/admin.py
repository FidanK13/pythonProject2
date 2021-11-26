from django.contrib import admin
from .models import PostModel, CustomUser

# Register your models here.
admin.site.register(PostModel)
admin.site.register(CustomUser)