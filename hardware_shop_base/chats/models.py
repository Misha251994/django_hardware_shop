from django.db import models
from django.contrib.auth.models import User


class Chat (models.Model):
    # Message model

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_message")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)
