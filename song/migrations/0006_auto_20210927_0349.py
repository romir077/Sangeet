# Generated by Django 3.2.6 on 2021-09-26 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0005_auto_20210927_0349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party_songs',
            name='audio_file',
        ),
        migrations.RemoveField(
            model_name='party_songs',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='party_songs',
            name='image',
        ),
        migrations.RemoveField(
            model_name='party_songs',
            name='title',
        ),
    ]
