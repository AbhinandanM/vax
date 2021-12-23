from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
import datetime
import requests
from .models import NotifyList, Notified_members
from django.core.mail import send_mail
from .forms import Notifyform
import time

# Create your views here.

def main(request):
    return render(request, 'main.html', {})

def search(request):
    try:
        pincode = request.GET.get('pincode')
        date = datetime.date.today().strftime('%d-%m-%Y')
        headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
        res = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={date}", headers=headers).json()
        data = res.items()
        try:
            age = int(request.GET.get('age'))
        except: 
            age = 45

        context = {
            'data': data,
            'pincode':pincode,
            'date':date,
            'age':age
        }
        return render(request, 'aa.html', context)
    except:
        return render(request, 'aa.html', {})

def success(request):
    
    return render(request, 'success.html', {})


def notify_form(request):
    try:
        if request.method == 'POST':
            form = Notifyform(request.POST)
            #print(form.errors)
            if form.is_valid():
                form.instance.Pincode = form.cleaned_data['Pincode']
                form.instance.Email = form.cleaned_data['Email']
                form.instance.Phone_no = form.cleaned_data['Phone_no']
                form.save()
                return redirect('http://cowinavailability.help/success/')
                 # does nothing, just trigger the validation
        else:
            form = Notifyform()
        context = {
            'form': form,
        }
        return render(request, 'notify_form.html', context)
    except:
        return render(request, 'notify_form.html', {'form': form,})








  