from django.urls import path

from . import views

app_name = 'mc'
urlpatterns = [
    path('info/', views.info, name='info'),
]
