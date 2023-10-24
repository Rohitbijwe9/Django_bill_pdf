from django.urls import  path
from .views import  *

urlpatterns=[
    path('bill/',bill,name='bill_url'),
    path('genbill/',generate_bill,name='genbill_url')
]