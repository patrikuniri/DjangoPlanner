# event_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('event_management.urls')),
    path('participants/', include('participant_management.urls')),  # Include participant_management URLs
]
