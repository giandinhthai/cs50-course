from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import render
def index(request):
    now=datetime.datetime.now()
    newyear_bool=False
    if now.day==1 and now.month==1:
        newyear_bool=True
    return render(request, "newyear/index.html",{
        "newyear_bool": newyear_bool
    })