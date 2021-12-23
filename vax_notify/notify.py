import requests
from .models import Notified_members, NotifyList
import datetime
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
import time

def notify():
    lis = NotifyList.objects.all()
    lll = []
    try:
        with open('/home/ubuntu/code/vax/vax_notify/pin.txt', 'r') as f:
            valid_pin = f.read()
        for i in lis:
            if str(i.Pincode) in valid_pin:
                lis_of_days = [0,7,14,21,28,35,42]
                count = 0
                for t in lis_of_days:
                    date = datetime.datetime.today() + datetime.timedelta(days=t)
                    Dates = date.strftime('%d-%m-%Y')
                    print(Dates)
                    headers = {'Host': 'cdn-api.co-vin.in', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
                    resttt = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={i.Pincode}&date={Dates}", headers=headers)
                    
                    if 'json' in resttt.headers.get('Content-Type'):
                        res = resttt.json()
                        for key,value in res.items():
                            if value == []:
                                print(i.Pincode, 'Data For this pincode is not available currently')
                            else:
                                if i.Email :
                                    subject, to = 'Vaccination Alert by CoWin-Helper', [f'{i.Email}']
                                    html_content = []
                                    m = f"Available Vaccination slots at Pincode: {i.Pincode}"

                                    for k in value:
                                        session = k['sessions'][0]
                                        name = k['name']
                                        fee = k['fee_type']
                                        cap = session['available_capacity']
                                        min_age_lim = session['min_age_limit']
                                        vaccine = session['vaccine']
                                        address = k['address']
                                        date = session['date']
                                        mes =f'<h2><b>Name:</b> {name}</h2>\n<h3><b>Vaccine:</b> {vaccine} --- <b>Min. Age Limit:</b> {min_age_lim}</h3>\n<p><strong>Fee Type:</strong> {fee} --- <strong>Available Capacity:</strong> {cap}</p>\n<p><strong>Date:</strong> {date} --- <strong>Address:</strong> {address}</p>\n<p><a href="https://selfregistration.cowin.gov.in"><b>Register Now</b></a> Or Visit <a href="https://selfregistration.cowin.gov.in"><b>Here</b></a> to Know More</p>'

                                        if cap > 5:

                                            html_content.append(mes)

                                        else:
                                            pass
                                        
                                    mesg = '] ['.join(str(x) for x in html_content)
                                    if len(mesg) > 15:

                                        send_mail(subject=subject, message=m, from_email='helper.cowin@gmail.com', recipient_list=to, html_message=mesg)
                                        count += 1
                                    else:
                                        pass

                    else:
                        print(resttt)
                        pass              
                if count >=1:
                    try:
                        post = get_object_or_404(NotifyList, id=i.pk)
                        alert_send_record = Notified_members.objects.create(pincode=i.Pincode, email= i.Email, phone_no = i.Phone_no)
                        print(count, "this is count")
                        post.delete()
                    except Exception as e:
                        print(e, "this is an erron here")
                        m = f"Task is crashed because : {e}"
                        recipient = ['mabhinandan41@gmail.com',]

                else:
                    pass
            else:
                print(i.Pincode, "this is not valid")
                post = get_object_or_404(NotifyList, id=i.pk)
                print(post, 'this is post')
                post.delete()
    except Exception as e:
        print(e, "this is exception")
        m = f"Task is crashed because : {e}"
        recipient = ['mabhinandan41@gmail.com',]
        



