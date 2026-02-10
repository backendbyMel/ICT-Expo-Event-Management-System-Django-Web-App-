from django.db import models
from users.models import Profile

class Customer(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Photo(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='photobooth_photos/')
    uploaded_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    printed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.name} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"