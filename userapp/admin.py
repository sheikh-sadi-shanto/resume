from django.contrib import admin
from userapp.models import *
# Register your models here.



class ok(admin.ModelAdmin):
    list_display=('user','id','title','adress','age','number','gander','cover_pic',)
admin.site.register(Profile,ok)

class con(admin.ModelAdmin):
    list_display=('name','email','message')
admin.site.register(Contact,con)

admin.site.register(Post_user)