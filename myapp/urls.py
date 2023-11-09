from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_real_time_data(), name='my_view'),
]
