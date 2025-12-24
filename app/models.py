from django.db import models

# Create your models here.

class Inse(models.Model):
    id=models.PositiveIntegerField(primary_key=True)
    name=models.CharField()
    email=models.CharField()
    salary=models.FloatField()
    
    def __str__ (self):
        s=str(self.id)
        return s
    
    