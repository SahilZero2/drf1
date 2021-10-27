from django.db import models

# Create your models here.
class advisor(models.Model):
    name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to = 'profile_picture/')

    def __str__(self):
        return self.name