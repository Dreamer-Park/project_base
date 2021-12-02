from django.db import models
from datetime import timedelta, date
from django.utils.timezone import now
# Create your models here.

def get_deadline():
    return now() + timedelta(days=364)

def get_startline():
    return date(2021, 12, 1)


class api_category(models.Model):
    category_name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    api_key_id_name = models.CharField(max_length=100,null=True)
    api_key_id_value  = models.CharField(max_length=100,null=True)
    api_key_main_name = models.CharField(max_length=100,default='')
    api_key_main_value = models.CharField(max_length=100,default='')
    api_admin_id = models.CharField(max_length=20, null=True)
    api_at_create= models.DateField(auto_now_add=True)
    api_duedate  = models.DateField(null=True,default=get_deadline())
    
    class Meta:
        unique_together = ["category_name"]
    
    def __str__(self):
        return self.category_name

class url_category(models.Model):
    category_name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    api_target_urls = models.CharField(max_length=100, null=True)
    class Meta:
        unique_together = ["category_name"]
    
    def __str__(self):
        return f"{self.category_name}:{self.api_target_urls:.05}"
    
class api_key(models.Model):
    api_name = models.CharField(max_length=20)
    api_service_category = models.ForeignKey(api_category, on_delete=models.CASCADE, null=True)
    api_url_service = models.ForeignKey(url_category, on_delete=models.CASCADE, null=True)
    api_key_status = models.BooleanField(default=True)
    
    
    
    

    
    
    