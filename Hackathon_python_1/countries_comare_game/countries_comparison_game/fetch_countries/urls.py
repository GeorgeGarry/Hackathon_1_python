from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('main/', views.generate_main_page, name="generate_main_page"),
    path('call_custom_function/', views.call_custom_function, name="call_custom_function")


]
