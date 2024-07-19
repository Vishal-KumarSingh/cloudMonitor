from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import logout as log_out, login as log_in
from django.contrib.auth.decorators import login_required
from cmdHelper.lib import *
import json
from . import models
# Create your views here.


def index(request):
    if (request.user.is_authenticated):
        return redirect('home')
    return redirect('login')

@login_required
def home(request):
    # if not (request.user.is_authenticated):
    #     return redirect('login')
    return render(request, 'welcome.html')


@login_required
def dashboard(request):
    systeminfo = getStaticSystemInformation()
    print(type(systeminfo))
    return render(request, 'welcome.html' , systeminfo)

@login_required
def scriptrunner(request):
    scripts = models.Sripts.objects.all()
    return render(request, 'scriptrunner.html' , {'scripts' : scripts})

@login_required
def executeCommand(request):
    cmd = request.POST.get('cmd')
    output = execCMD(cmd)
    return HttpResponse(output)

@login_required
def applicationstore(request):
    application = models.Application.objects.all()
    for app in application:
        output = execCMD("which "+app.softwarename)
        if output == "":
            app.status = "Not Installed"
        else:
            app.status = "Installed"
    return render(request, 'applicationstore.html' , {'application' : application})
@login_required
def codeeditor(request):
    systeminfo = getStaticSystemInformation()
    path = request.GET.get('path')
    edit = request.GET.get('edit')
    fullpath = path + "/" + edit
    data = execCMD(["cat "+ fullpath ])
    return render(request, 'codeeditor.html' , {"data":data , "path":fullpath})
@login_required
def deleteF(request):
    systeminfo = getStaticSystemInformation()
    print(type(systeminfo))
    return render(request, 'codeeditor.html' , systeminfo)

@login_required
def saveFile(request):
    data = request.POST.get('data')
    path = request.POST.get('path')
    # Open a file for writing ('w' mode creates a new file or truncates an existing file)
    with open(path , 'w') as f:
        f.write(data)  # Write a string to the file
    return render(request, 'codeeditor.html' , {"data":"File Saved Successfully"})

@login_required
def settings(request):
    systeminfo = getStaticSystemInformation()
    print(type(systeminfo))
    return render(request, 'settings.html' , systeminfo)

@login_required
def commandhistoryapi(request):
    history = execCMD("cat ~/.bash_history")
    print(history)
    return HttpResponse(json.dumps(history.splitlines()))


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
def taskmanagerapi(request):
    tasks = getTaskManager()
    print(tasks)
    return HttpResponse(json.dumps(tasks.splitlines()))
@login_required
def killprocess(request):
    id = request.POST.get('id')
    tasks = execCMD("kill "+id)
    return HttpResponse(json.dumps(tasks))

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

def experiment(request):
    return HttpResponse(execCMD("sudo ls -l"))