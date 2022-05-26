from django.contrib import admin

# Register your models here.
from .models import Post, SiteUser

admin.site.register(Post)
admin.site.register(SiteUser)