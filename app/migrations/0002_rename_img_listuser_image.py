# Generated by Django 3.2.9 on 2021-11-16 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listuser',
            old_name='img',
            new_name='image',
        ),
    ]