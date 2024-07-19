from django.shortcuts import render,HttpResponse

# Create your views here.
from cmdHelper.lib import *
import json
def index(request):
    output = execCMD('systemctl list-units --all  --no-pager --no-legend --type=service')
    lines = output.strip().split('\n')
    services_array = []
    for line in lines:
         columns = line.split()
         services_array.append(columns)
    return render(request , "services.html" , { 'services' : services_array })

def listServices(request):
    return  HttpResponse("")