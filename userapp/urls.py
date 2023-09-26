
from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',loginview,name='login'),
    path('register',register,name='register'),
    path('home',user_post,name='home'),
    path('edit',pro_edit,name='edit'),
    path('pro',profile,name='pro'),
    path('logout',log_out,name='logout'),
    path('sheikh',sheikh),
    path('pass',passchange,name='passwordchange')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
