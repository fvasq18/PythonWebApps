from django.db import models

# Create your models here.
class Superhero(models.Model):
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    description = models.TextField()
    strength = models.CharField(max_length=100)
    weakness = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'hero'

    def __str__(self):
        return f'{self.pk}. {self.name} - {self.description}'