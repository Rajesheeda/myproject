from django.conf.urls import url
from . import views
app_name = "try_first"
urlpatterns=[
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
    # /try_first/album/add
    url(r'album/add/$',views.AlbumCreate.as_view(), name='album-add'),

    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    # /try_first/2/update
  #  url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /try_first/2/delete
 #   url(r'album/(?P<pk>[0-9]+)/$', views.AlbumDelete.as_view(), name='album-delete'),

#    url(r'^$', views.index,name='index'),
    #/try_first/12/
#    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name="detail"),
#/try_first/12/favourite
#    url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name="favorite"),
]