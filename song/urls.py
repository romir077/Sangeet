from django.contrib import admin
from django.urls import path
from song import views

urlpatterns = [
    path('',views.index, name="index"),
    path('mix',views.mix_song, name="mix"),
    path('chill',views.chill_song, name="chill"),
    path('party',views.party_song, name="party"),
    path('arijit',views.arijit_singh, name="arijit"),
    path('jubin',views.jubin_nautiyal, name="jubin"),
    path('rahman',views.a_r_rahman, name="rahman"),
    path('test',views.test, name="test")
]