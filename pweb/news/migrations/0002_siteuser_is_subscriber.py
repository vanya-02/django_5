# Generated by Django 4.0.4 on 2022-05-26 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='is_subscriber',
            field=models.BooleanField(default=False),
        ),
    ]