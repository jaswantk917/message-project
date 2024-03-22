from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail

def send_message_email(message, contact_info):
    subject = f'New Message Received from {contact_info}'
    body = f'Message: {message}\nContact Info (Optional): {contact_info}'
    sender_email = 'jaswantk917@yahoo.com'
    recipient_list = ['jaswantk917@gmail.com']  # Send to yourself
    print(f'Sending email to {recipient_list}', flush=True)
    send_mail(subject, body, sender_email, recipient_list)

def index(request):

    return HttpResponse(b"Hello, world. You're at the index.")


# @permission_classes([AllowAny])
# @api_view(['POST'])
@csrf_exempt
def submit_message(request):
    if request.method == 'POST':
        print(request.body, flush=True)
        raw_data = request.body.decode('utf-8')  # Decode the byte string
        data = json.loads(raw_data)
        message = data.get('message')
        contact_info = data.get('contactInfo')
        try:
            send_message_email(message, contact_info)
            return JsonResponse({'success': True})
        except Exception as e:
            print(str(e), flush=True)
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
