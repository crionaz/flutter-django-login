from django.urls import path, include
from api import views


urlpatterns = [
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
    path('home',views.home)
    # path('home/',views.home),

]