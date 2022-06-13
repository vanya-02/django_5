from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class SiteUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    is_user = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)

    def get_id(self):
        return f"{self.id}"

    class Meta:
        ordering = ['-date_added']

class App(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)

    def get_id(self):
        return f"{self.id}"

    class Meta:
        ordering = ['-date_added']

