from django.urls import path
from django.shortcuts import render


namespace = 'playground'

urlpatterns = [
    path('', lambda request: render(request, 'playground/index.html'), name='welcome'),
]
