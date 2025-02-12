from django.db import models

class Music(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    audio = models.FileField(upload_to='music/audio')
   

    
    def __str__(self):
        return self.name
