from django.db import models
from authentication.models import User
import datetime
# Create your models here.
# create Leave model


class Leave(models.Model):
    date_from = models.DateField(default=datetime.date.today)
    date_to = models.DateField(default=datetime.date.today)
    leave_status = (
        ('select', 'select'),
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('cancel', 'cancel'),
        ('reject', 'reject'), )
    status = models.CharField(choices=leave_status, default="select", max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

    def _str__(self):
        return self.status
   

# Create model Feedback


class Feedback(models.Model):
    
    content = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def _str__(self):
        return self.content
