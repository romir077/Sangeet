from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from . models import Mix_Songs


def index(request):
    return render(request,'index.html')
    # return HttpResponse("this is index !")

def mix_song(request):
    paginator= Paginator(Mix_Songs.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"mix_songs.html",context)

def chill_song(request):
    paginator= Paginator(Mix_Songs.objects.filter(song_type="Chill"),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"chill_songs.html",context)

def party_song(request):
    paginator= Paginator(Mix_Songs.objects.filter(song_type="Party"),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"party_songs.html",context)

def jubin_nautiyal(request):
    paginator= Paginator(Mix_Songs.objects.filter(artist_name="Jubin Nautiyal"),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"jubin_nautiyal.html",context)

def arijit_singh(request):
    paginator= Paginator(Mix_Songs.objects.filter(artist_name="Arijit Singh"),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"arijit_singh.html",context)

def test(request):
    paginator= Paginator(Mix_Songs.objects.filter(artist_name="Arijit Singh"),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"test.html",context)

def a_r_rahman(request):
    paginator= Paginator(Mix_Songs.objects.filter(artist_name="A R Rahman"),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # while(page_obj[0].artist_name != "A R Rahman"):
    #     page_number=str(int(page_number)+1)
    #     if(int(page_number)>21):
    #         break
    #     page_obj = paginator.get_page(page_number)
    
    context={"page_obj":page_obj}
    print(type(page_number),page_number)
    return render(request,"a_r_rahman.html",context)
