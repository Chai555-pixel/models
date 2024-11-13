from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)  # Custom primary key
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'posts'  # Custom table name
