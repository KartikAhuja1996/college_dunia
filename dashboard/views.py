import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import time
# Create your views here.



def index(request): 
    ts = time.time()
    context = {
        "timestamp":time.strftime("%d/%m/%Y %I:%M:%S %p %Z", time.gmtime(ts))
    }    
    return render(request,"home.html",context=context)