# Generated by Django 4.2.7 on 2023-12-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_namecount'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isConfirmed',
            field=models.BooleanField(default=False),
        ),
    ]
