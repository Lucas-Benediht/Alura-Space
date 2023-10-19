
from django.contrib import admin
from django.urls import path, include


# Urls para atender na aplicação 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
]
