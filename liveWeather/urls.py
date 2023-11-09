from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('liveWeather.urls')),
    path('real-time-data/', views.real_time_data, name='real_time_data'),
]
