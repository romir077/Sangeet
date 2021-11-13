# Generated by Django 3.2.6 on 2021-09-11 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_partysongs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party_Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='')),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Workout_Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='')),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Partysongs',
            new_name='Chill_Songs',
        ),
        migrations.RenameModel(
            old_name='Song',
            new_name='Mix_Songs',
        ),
    ]