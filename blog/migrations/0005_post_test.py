# Generated by Django 3.2.15 on 2022-09-07 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test',
            field=models.CharField(default='unknown', max_length=50),
        ),
    ]