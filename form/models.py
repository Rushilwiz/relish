from django.db import models

# Create your models here.
class Response(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'
        ordering = ['created_at']
