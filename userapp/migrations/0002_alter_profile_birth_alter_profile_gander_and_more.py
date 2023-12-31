# Generated by Django 4.1.7 on 2023-09-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gander',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='pic'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
