# Generated by Django 3.2.7 on 2021-10-13 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0004_remove_cooluser_gh_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='chart_link',
        ),
    ]
