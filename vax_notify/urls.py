from django.urls import path
from .views import main, search, notify_form, success
urlpatterns = [
    path('', main, name="main_page"),
    path('result/', search, name="search"),
    #path('list/', listing, name="list"),
    path('get-notified/', notify_form, name="notify-form"),
    path('success/', success, name="success-page")
]