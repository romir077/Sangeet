from django.db import models
from django.db.models.deletion import CASCADE

class Mix_Songs(models.Model):
    title= models.CharField(max_length=100)
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    duration=models.CharField(max_length=25)
    artist_name = models.CharField(max_length=25,default="null")
    song_type = models.CharField(max_length=25,default="null")
    paginate_by = 20

    def __str__(self):
        return self.title







    

# class Party_Songs(models.Model):
#     song_party = models.ForeignKey(Mix_Songs, on_delete=CASCADE, null=True)
#     party_song_name = models.TextField(null=True)

# class Chill_Songs(models.Model):
#     song_chill = models.ForeignKey(Mix_Songs, on_delete=CASCADE, null=True)
#     chill_song_name = models.TextField(null=True)

# class Extra_info (models.Model):
#     movie_name = models.CharField(max_length=25)
#     artist_name = models.CharField(max_length=25)
#     year_release = models.IntegerField()
#     song_id_artist = models.ForeignKey(Mix_Songs, on_delete=CASCADE)
        

# class Arijit_Singh (models.Model):
#     Arijit_Songs = models.ForeignKey(Mix_Songs, on_delete=CASCADE)
#     Arijit_Songs_extra = models.ForeignKey(Extra_info, on_delete=CASCADE)
#     song_name_arijit = models.CharField(max_length=25)

# class A_R_Rahman (models.Model):
#     Rahman_songs = models.ForeignKey(Mix_Songs, on_delete=CASCADE)
#     Rahman_songs_extra = models.ForeignKey(Extra_info, on_delete=CASCADE)
#     song_name_rahman = models.CharField(max_length=25)

# class Jubin_Nautiyal (models.Model):
#     Jubin_songs = models.ForeignKey(Mix_Songs, on_delete=CASCADE)
#     Jubin_songs_extra = models.ForeignKey(Extra_info, on_delete=CASCADE)
#     song_name_jubin = models.CharField(max_length=25)
