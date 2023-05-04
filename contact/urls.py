from django.urls import path
from contact import views

appname = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]
