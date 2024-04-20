from django.urls import path
from .views import submit_message, get_all_messages

urlpatterns = [
    path('/', submit_message, name='hello_world'),
    path('submit-message/', submit_message, name='submit_message'),
    path('get-all-messages/', get_all_messages, name='get_all_messages'),


]
