from django.db import models


class Team(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=2, null=True)
    country = models.CharField(max_length=255, null=True)
    coach = models.CharField(max_length=255, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
