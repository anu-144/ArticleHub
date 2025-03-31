from django.urls import path
from. import views

urlpatterns = [
    path('home6/', views.home6,name='home6'),
    path('contact6/', views.contact6,name='contact6'),
    path('about6/', views.about6,name='about6'),
    path('article/<int:id>/', views.article,name='article'),
]