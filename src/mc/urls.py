from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('info/', views.info, name='info'),
]
