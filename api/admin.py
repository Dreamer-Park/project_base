from django.contrib import admin
from api.models import api_category,api_key,url_category
# Register your models here. 



admin.site.register(api_category)
admin.site.register(url_category)
admin.site.register(api_key)


