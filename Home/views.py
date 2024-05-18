from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import logout as log_out, login as log_in
from django.contrib.auth.decorators import login_required
from cmdHelper.lib import *
import json
# Create your views here.
@login_required
def home(request):
    # if not (request.user.is_authenticated):
    #     return redirect('login')
    return render(request, 'index.html')


@login_required
def dashboard(request):
    systeminfo = getStaticSystemInformation()
    print(type(systeminfo))
    return render(request, 'dashboard.html' , systeminfo)
@login_required
def scriptrunner(request):
    systeminfo = getStaticSystemInformation()
    print(type(systeminfo))
    return render(request, 'scriptrunner.html' , systeminfo)
@login_required
def settings(request):
    systeminfo = getStaticSystemInformation()
    print(type(systeminfo))
    return render(request, 'settings.html' , systeminfo)
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


@login_required
def taskmanager(request):
    systeminfo = getStaticSystemInformation()
    print(type(systeminfo))
    return render(request, 'taskmanager.html' , systeminfo)
@login_required
def shell(request):
    systeminfo = getStaticSystemInformation()
    print(type(systeminfo))
    return render(request, 'shell.html' , systeminfo)
@login_required
def commandhistory(request):
    systeminfo = getStaticSystemInformation()
    print(type(systeminfo))
    return render(request, 'commandhistory.html' , systeminfo)

@login_required
def resourceusage(request):
    usage = getSystemUsage()
    print(usage)
    return HttpResponse(json.dumps(usage))

@login_required
def executeShellCMD(request):
    print(request.POST)
    cmd = request.POST.get('cmd')
    print(cmd)
    SSHSession.input += cmd
    # print(usage)
    return HttpResponse("")

@login_required
def getOutput(request):
    # print(usage)
    return HttpResponse(SSHSession.getOutput())


def logout(request):
    if (request.user.is_authenticated):
        log_out(request)
    return redirect('login')
    


def login(request):
    if (request.user.is_authenticated):
        return redirect('home')
    if request.method == 'GET':
        return render(request, 'login.html')
    email = request.POST['email']
    password = request.POST['password']
    print(email)
    print(password)
    user = authenticate(username=email, password=password)
    if user is not None:
        log_in(request, user)
        return redirect('home')
    else:
        return render(request, 'login.html', {'error': 'Invalid login credentials'})
def reset(request):
    if (request.user.is_authenticated):
        return redirect('home')
    return render(request, 'resetPassword.html')

from cmdHelper.lib import execCMD
def experiment(request):
    return HttpResponse(execCMD("sudo ls -l"))