from django.db import models
from django.conf import settings


class Message(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "messanger"

    def __str__(self):
        return f"Message from {self.user.username} at {self.created_at}"
