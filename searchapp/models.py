from django.db import models

# Create your models here.

class BioData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    nationality = models.CharField(max_length=200, blank=True, null=True)
    
    
    
    class Meta:
        verbose_name = 'Bio-Data'
        verbose_name_plural = 'Bio-Datas'



    def __str__(self):
        return self.first_name