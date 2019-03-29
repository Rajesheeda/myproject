#from django.http import Http404
#from django.http import HttpResponse
#from django.template import loader
#from . models import Album,Song

# Create your views here.
#def index(request):
#    all_album=Album.objects.all()
#    template=loader.get_template("try_first/index.html")
#    context={'all_album':all_album }
#    return  HttpResponse(template.render(context,request))

#def detail(request,album_id):
#    album=get_object_or_404(Album,pk=album_id)

##   try:
##        album=Album.objects.get(pk=album_id)
##   except:
##        raise Http404("Album dosen't exist")
#    return  render(request,'try_first/detail.html',{'album':album})

##return  HttpResponse("<h2>details for album_id :" + str(album_id) + "</h2>")

#def favorite(request,album_id):
#    album = get_object_or_404(Album, pk=album_id)
#    try:
#        selected_song=album.song_set.get(pk=request.POST['song'])
#    except:
#        return render(request,'try_first/detail.html',{
#            'album':album,
#            'error_message':"You didnot selected a valis song",
#
#        })
#    else:
#        selected_song.is_favorite=True
#        selected_song.save()
#        return render(request, 'try_first/detail.html', {'album': album})

from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import  reverse_lazy

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
#from .forms import AlbumForm, SongForm, UserForm
from .models import Album, Song
from .models import Album


class IndexView(generic.ListView):
    template_name="try_first/index.html"
    context_object_name = "all_album"

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name ="try_first/detail.html"

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

def AlbumDelete(request, album_id):
    model=Album
    album = Album.objects.get(pk=album_id)
    album.delete()
    albums = Album.objects.filter(user=request.user)
    return render(request, 'music/index.html', {'albums': albums})


def favorite(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})