from django.urls import path
from . import views

app_name = 'participant_management'

urlpatterns = [
    path('register/', views.register_participant, name='register_participant'),
    path('accept/<int:participant_id>/', views.accept, name='accept'),
    path('decline/<int:participant_id>/', views.decline, name='decline'),
]
