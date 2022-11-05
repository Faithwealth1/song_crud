from rest_framework import serializers
# from .models import Song, Artiste, Lyrics
from .models import Song, Lyrics


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'artiste', 'likes', 'release_date')
    
# class SongSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     artist = serializers.CharField(max_length=100)
#     likes = serializers.IntegerField()
#     release_date = serializers.DateField()
    
    
class LyricsSerializer(serializers.Serializer):
    song = SongSerializer()
    content = serializers.CharField()
    

# class ArtisteSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     age = serializers.IntegerField()
#     songs = SongSerializer(many=True)
#     lyrics = LyricsSerializer(many=True)