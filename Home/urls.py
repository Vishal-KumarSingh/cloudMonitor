"""
URL configuration for cloudwatch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path , include
from . import views
urlpatterns = [
     path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('reset', views.reset , name='reset'),
    path('logout', views.logout , name='logout'),
    path('dashboard', views.dashboard , name='dashboard'),
    path('api', views.experiment , name='api'),
    path('resourceusage', views.resourceusage , name='resourceusage'),
    path('taskmanager', views.taskmanager , name='taskmanager'),
   
    path('settings', views.settings , name='settings'),
    path('scriptrunner', views.scriptrunner , name='scriptrunner'),
    path('shell', views.shell , name='shell'),
    path('executeShellCMD', views.executeShellCMD , name='executeShellCMD'),
    path('commandhistory', views.commandhistory , name='commandhistory'),
    path('applicationstore', views.applicationstore , name='applicationstore'),
     path('commandhistoryapi', views.commandhistoryapi , name='commandhistoryapi'),
    path('taskmanagerapi', views.taskmanagerapi , name='taskmanagerapi'),
      path('killprocess', views.killprocess , name='killprocess'),
        path('codeeditor', views.codeeditor , name='codeeditor'),
         path('deleteF', views.deleteF , name='deleteF'),
         path('saveFile', views.saveFile , name='saveFile'),
   
    
]
