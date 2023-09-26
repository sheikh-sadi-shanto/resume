# Generated by Django 4.2.5 on 2023-09-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0012_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_pic',
            field=models.ImageField(blank=True, default='media/default.png', null=True, upload_to='pic'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pro_pic',
            field=models.ImageField(blank=True, default='media/default.png', null=True, upload_to='pro_pic'),
        ),
    ]