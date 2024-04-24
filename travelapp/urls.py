from django.urls import path
from . import views
app_name = 'travelapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    #path('add/', views.addition, name='addition'),

    #path('about/',views.about,name='about'),
  #path('contact/',views.contact,name='contact'),

]
