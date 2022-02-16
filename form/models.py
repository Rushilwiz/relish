from django.db import models
from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Response(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    address = AddressField(on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'
        ordering = ['created_at']
