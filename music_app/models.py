from django.db import models
import uuid

# class Artiste(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     age = models.IntegerField()

class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    artiste = models.CharField(max_length=50)
    # artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    likes = models.FloatField()
    release_date = models.DateField()
    
    def __str__(self):
        return self.title
    
    
class Lyrics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    song = models.OneToOneField(Song, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.song.title