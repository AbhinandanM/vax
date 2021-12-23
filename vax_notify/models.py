from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class NotifyList(models.Model):
    Pincode = models.IntegerField()
    Email = models.EmailField(blank=True, null=True)
    Phone_no = models.CharField(max_length=10, blank=True, null=True)
    Date = DateField(auto_now_add=True)

    def __str__(self):
        return str(self.Email)

class Notified_members(models.Model):
    pincode = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    phone_no = models.CharField(max_length=10 ,blank=True, null=True)
    date = DateField(auto_now_add=True)

    def __str__(self):
        return str(self.email)