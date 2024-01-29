from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_event/', views.create_event, name='add_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('delete_participant/<int:participant_id>/', views.delete_participant, name='delete_participant'),
    
]

