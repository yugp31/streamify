from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class MediaContent(models.Model):
    MEDIA_TYPES = (
        ('video', 'Video'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = CloudinaryField('file', resource_type='video')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='video')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ai_generated = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.ForeignKey(MediaContent, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.content.title}"

