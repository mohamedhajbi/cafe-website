# Generated by Django 4.0.5 on 2022-09-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='img',
            field=models.ImageField(null=True, upload_to='rooms_imgs/'),
        ),
    ]
