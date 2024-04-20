from django.urls import path
from .views import submit_message, get_all_messages, index

urlpatterns = [
    path('', index, name='hello_world'), # This is the root path
    path('submit-message/', submit_message, name='submit_message'),
    path('get-all-messages/', get_all_messages, name='get_all_messages'),


]
