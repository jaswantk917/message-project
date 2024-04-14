from django.db import models

# Create your models here.

# Define the comment model
class Comment(models.Model):
    user_uuid = models.CharField(max_length=36)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
