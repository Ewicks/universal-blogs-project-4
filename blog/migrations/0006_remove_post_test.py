# Generated by Django 3.2.15 on 2022-09-07 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='test',
        ),
    ]