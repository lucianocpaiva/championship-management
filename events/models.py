from django.db import models

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    match = models.ForeignKey('matches.Match', on_delete=models.CASCADE, related_name='match')
    
    def __str__(self):
        return self.title 

