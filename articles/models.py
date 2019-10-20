from django.db import models

class Comment(models.Model):
    article_uuid = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.body} -- {self.created_at}'