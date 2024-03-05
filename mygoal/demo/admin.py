from django.contrib import admin
from.import models
# Register your models here.
    
    
class bannerAdmin(admin.ModelAdmin):
    list_display = ['img','tital','content','para1','para2']
admin.site.register(models.banner)

class Testmodeladmin(admin.ModelAdmin):
    list_display = ['email']
admin.site.register(models.TestModel)

class blog1Admin(admin.ModelAdmin):
    list_display = ['image1','date','cont1','paragraph']
admin.site.register(models.blog1)



    
