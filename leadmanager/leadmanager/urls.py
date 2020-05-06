from django.contrib import admin
from django.urls import path, include

# importing "include" from 'django.urls' allows to include a separate file

urlpatterns = [
    path('', include('leads.urls')),
]
