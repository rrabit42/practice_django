# Generated by Django 2.1.5 on 2019-02-03 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d'),
        ),
    ]
