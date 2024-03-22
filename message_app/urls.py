from django.urls import path
from .views import submit_message

urlpatterns = [
    path('submit-message/', submit_message, name='submit_message'),
]
