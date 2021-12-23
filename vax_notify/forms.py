from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import NotifyList

class Notifyform(ModelForm):
    class Meta:
        model = NotifyList
        fields = '__all__'