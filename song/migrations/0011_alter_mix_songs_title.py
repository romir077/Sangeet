# Generated by Django 3.2.6 on 2021-11-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0010_auto_20211109_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mix_songs',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
