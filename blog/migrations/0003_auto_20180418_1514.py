# Generated by Django 2.0.4 on 2018-04-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.TextField(blank=True),
        ),
    ]
