from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Meta:
    ordering = ['-created_at']
