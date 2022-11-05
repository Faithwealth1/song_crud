from django.urls import path, include
from .views import (MusicList, MusicDetail, AddMusic, LyricsDetail, LyricsList)


urlpatterns = [
    path("songs/", MusicList.as_view(), name="music_list"),
    path("song/add/", AddMusic.as_view(), name="add_music"),
    path("song/<int:pk>/", MusicDetail.as_view(), name="music_detail"),
    path("song/<int:pk>/lyrics/", LyricsDetail.as_view(), name="lyrics_detail"),
]
