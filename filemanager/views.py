from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import logout as log_out, login as log_in
from django.contrib.auth.decorators import login_required
from cmdHelper.lib import *
import json
# Create your views here.
def index(request):
    if (request.user.is_authenticated):
        return redirect('home')
    return redirect('login')

@login_required
def filemanager(request):
    systeminfo = getStaticSystemInformation()
    print(type(systeminfo))
    return render(request, 'filemanager.html' , systeminfo)

@login_required
def filemanagerapi(request):
    location = request.POST.get('location')
    print(location)
    files = execCMD(["ls -l "+ location ])
    return HttpResponse(json.dumps(files.splitlines()))
