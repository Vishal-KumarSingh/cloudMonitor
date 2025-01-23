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
    bookmarks = models.BookMarks.objects.all() #bookmarks db haii
    //database se access krne ke liye model  likhna prte hai 
    return render(request, 'filemanager.html' , {'bookmarks':bookmarks})
    # request ,html file name,r knsa data dena haii
    #yeah bookmark  list of object hai 

@login_required
def filemanagerapi(request):
    location = request.POST.get('location')
    #ui se location le rhe haii
    print(location)
    files = execCMD(["ls -l "+ location ])
    #ls-l gives whole file list 
    return HttpResponse(json.dumps(files.splitlines()))


@login_required
def createFolder(request):
    foldername = request.POST.get('foldername')
    output = execCMD("sudo mkdir '"+foldername+"'")
    #mkdir se naya folder bna do
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
      
