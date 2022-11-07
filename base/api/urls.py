from django import urls
from django.urls import path
from . import views

urlpatterns=[
    path('',views.getRoutes),
    path('rooms/',views.getRooms),
    path('rooms/<slug:pk>/',views.getRoom),
    path('<str:word>/',views.getWord),

]