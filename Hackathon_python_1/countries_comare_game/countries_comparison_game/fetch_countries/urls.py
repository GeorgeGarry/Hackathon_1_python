from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('main/', views.generate_main_page, name="generate_main_page"),
    path('next-move/', views.next_move, name="next-move"),
]
