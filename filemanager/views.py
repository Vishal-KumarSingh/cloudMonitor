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
def filemanager(request):
    bookmarks = models.BookMarks.objects.all()
    return render(request, 'filemanager.html' , {'bookmarks':bookmarks})

@login_required
def filemanagerapi(request):
    location = request.POST.get('location')
    print(location)
    files = execCMD(["ls -l "+ location ])
    return HttpResponse(json.dumps(files.splitlines()))


@login_required
def createFolder(request):
    foldername = request.POST.get('foldername')
    output = execCMD("sudo mkdir '"+foldername+"'")
    return HttpResponse(output)
    
    
@login_required
def createNewFile(request):
    fielname = request.POST.get('filename')
    file = open(fielname , "w") 
    file.close()
    return HttpResponse("File created successfully ")
  
    
@login_required
def createBookMark(request):
    bookmarkName = request.POST.get('bookmarkName')
    folder = request.POST.get('folder')
    bookmark = models.BookMarks()
    bookmark.path = folder
    bookmark.name = bookmarkName
    # print(folder)
    # print(bookmark.name)
    bookmark.save()
    return HttpResponse("BookMark created successfully ")
      