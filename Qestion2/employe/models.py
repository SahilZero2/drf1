from django.db import models

# Create your models here.
class employe(models.Model):
    employe_name = models.CharField(max_length=30)
    salary = models.IntegerField()


    def __str__(self):
        return self.employe_name