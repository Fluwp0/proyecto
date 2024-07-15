from django.urls import path
from . import views

app_name = 'autos'

urlpatterns = [
    path('', views.modelos, name='modelos'),
    path('index/<int:id>/', views.index, name='index'),

]
