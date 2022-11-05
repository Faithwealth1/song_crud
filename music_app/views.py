from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Song
# from .serializer import SongSerializer, ArtisteSerializer, LyricsSerializer
from .serializer import SongSerializer, LyricsSerializer



class MusicList(APIView):
    """Display a list of all songs."""
    
    def get(self, request):
        """Return a list of all songs."""
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    

class MusicDetail(APIView):
    """Display a single song."""
    serializer_class = SongSerializer
    
    def post(self, request):
        """Add a new song."""
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        """Return a single song."""
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """Update a single song."""
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Delete a single song."""
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddMusic(APIView):
    """Add a new song."""
    serializer_class = SongSerializer
    
    def post(self, request):
        """Add a new song."""
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LyricsList(APIView):
    """Create and return a new `Lyrics` instance, given the validated data."""
    
    def get(self, request):
        """Get all lyrics"""
        lyrics = Lyrics.objects.all()
        serializer = LyricsSerializer(lyrics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """Create a new lyrics instance."""
        serializer = LyricsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LyricsDetail(APIView):
    """Get a single lyrics instance."""
    
    def get(self, request, pk):
        """Get a single lyrics instance."""
        lyrics = Lyrics.objects.get(pk=pk)
        serializer = LyricsSerializer(lyrics)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        """Update a single lyrics instance."""
        lyrics = Lyrics.objects.get(pk=pk)
        serializer = LyricsSerializer(lyrics, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Delete a single lyrics instance."""
        lyrics = Lyrics.objects.get(pk=pk)
        lyrics.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class ArtisteList(APIView):
#     """Create and return a new `Artiste` instance, given the validated data."""
    
#     def get(self, request):
#         """Return a list of all existing artists."""
#         artistes = Artiste.objects.all()
#         serializer = ArtisteSerializer(artistes, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         """Create a new artiste instance."""
#         serializer = ArtisteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# class ArtisteDetail(APIView):
#     """Return a `Artiste` instance."""
    
#     def get_object(self, pk):
#         try:
#             return Artiste.objects.get(pk=pk)
#         except Artiste.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk):
#         """Return an artiste instance."""
#         artiste = self.get_object(pk)
#         serializer = ArtisteSerializer(artiste)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         """Update an existing Artiste"""
#         artiste = self.get_object(pk)
#         serializer = ArtisteSerializer(artiste, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         """Delete an existing Artiste"""
#         artiste = self.get_object(pk)
#         artiste.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
