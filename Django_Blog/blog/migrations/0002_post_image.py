# Generated by Django 4.2.6 on 2023-10-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='intruder_image/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
