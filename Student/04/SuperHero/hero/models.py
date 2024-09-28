from django.db import models

# Create your models here.
class Superhero(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)

    class Meta:
        app_label = 'hero'

    def __str__(self):
        return f'{self.pk}. {self.name} - {self.description}'
