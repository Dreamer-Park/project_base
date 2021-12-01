from codecs import IncrementalDecoder
from django.db import models
from django.forms import CharField

# Create your models here.
class api_keys(models.Model):
    api_code=models.IntegerField(primary_key=True)
    api_name=models.CharField(max_length=20)
    
class api_key(models.Model):
    api_code=models.ForeignKey("api_code", related_name="code")
    api_order=models.AutoField(primary_key="True")
    key=models.CharField(max_length=50)
    
    

    
    
    