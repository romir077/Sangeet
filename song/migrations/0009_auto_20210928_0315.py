# Generated by Django 3.2.6 on 2021-09-27 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0008_remove_mix_songs_song_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='A_R_Rahman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name_rahman', models.CharField(max_length=25)),
                ('Rahman_songs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song.mix_songs')),
            ],
        ),
        migrations.CreateModel(
            name='Arijit_Singh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name_arijit', models.CharField(max_length=25)),
                ('Arijit_Songs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song.mix_songs')),
            ],
        ),
        migrations.CreateModel(
            name='Extra_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=25)),
                ('artist_name', models.CharField(max_length=25)),
                ('year_release', models.IntegerField()),
                ('song_id_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song.mix_songs')),
            ],
        ),
        migrations.CreateModel(
            name='Jubin_Nautiyal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name_jubin', models.CharField(max_length=25)),
                ('Jubin_songs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song.mix_songs')),
                ('Jubin_songs_extra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song.extra_info')),
            ],
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.AddField(
            model_name='arijit_singh',
            name='Arijit_Songs_extra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song.extra_info'),
        ),
        migrations.AddField(
            model_name='a_r_rahman',
            name='Rahman_songs_extra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song.extra_info'),
        ),
    ]