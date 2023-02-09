from django.db import models

# Create your models here.


class SupportStaff(models.Model):

    info = models.CharField(max_length=500)
    name = models.CharField(max_length=500, default=0)
    phone = models.CharField(max_length=150, default=0)
    whatsapp = models.CharField(max_length=50, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
