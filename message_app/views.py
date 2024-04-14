from django.core.serializers.json import uuid
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
from django.core.mail import send_mail
from django.middleware import csrf
from .models import Comment

def send_message_email(message, contact_info):
    subject = f'New Message Received from {contact_info}'
    body = f'Message: {message}\nContact Info (Optional): {contact_info}'
    sender_email = 'jaswantk917@yahoo.com'
    recipient_list = ['jaswantk917@gmail.com']  # Send to yourself
    print(f'Sending email to {recipient_list}', flush=True)
    send_mail(subject, body, sender_email, recipient_list)

def index(request):
    return HttpResponse(b"Hello, world. You're at the index.")


def submit_message(request):
    

    if request.method == 'POST':
        print(request.body, flush=True)
        raw_data = request.body.decode('utf-8')  # Decode the byte string
        if not raw_data:
            return JsonResponse({'success': False, 'error': 'No data provided'})
        data = json.loads(raw_data)
        message = data.get('message')
        contact_info = data.get('contactInfo')
        isPublic = data.get('isPublic') # make use of it
        if isPublic:
            user = data.get('user_uuid')
            try:
                Comment.objects.create(content=message, created_at=timezone.now(), user_uuid=user)
                return JsonResponse({'success': True})
            except Exception as e:
                print(str(e), flush=True)
                # dont sent 200 status code
                return JsonResponse({'success': False, 'error': str(e)})

        else: 
            try:
                send_message_email(message, contact_info)
                return JsonResponse({'success': True})
            except Exception as e:
                print(str(e), flush=True)
                return JsonResponse({'success': False, 'error': str(e)})
    
    elif request.method == 'GET':
        return JsonResponse({'csrfToken': csrf.get_token(request)
})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


def get_all_messages(request):
    comments = Comment.objects.all().order_by('-created_at')
    comments_list = []
    for comment in comments:
        comments_list.append({
            'content': comment.content,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'user_uuid': comment.user_uuid
        })
    return JsonResponse({'comments': comments_list})