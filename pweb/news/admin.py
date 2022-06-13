from django.contrib import admin

# Register your models here.
from .models import Game, App, SiteUser

admin.site.register(Game)
admin.site.register(SiteUser)
admin.site.register(App)