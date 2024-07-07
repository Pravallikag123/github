
#Greeting based on current time -GreetingApp

#Step 1: Activate the virtual environment

C:\djangoapps\myvenv\Scripts>activate

(myvenv) C:\djangoapps\myvenv\Scripts>cd..

(myvenv) C:\djangoapps\myvenv>cd..

#--------------------------------------------------------------------------------------------
#step 2: Creating or starting a project
(myvenv) C:\djangoapps>django-admin startproject myproj11

#--------------------------------------------------------------------------------------------
#step 3: Creating or starting a Application

(myvenv) C:\djangoapps\myproj11>py manage.py startapp GreetingApp

#----------------------------------------------------------------------------------------------
#Step 4: Goto Settings.py and add application to the installed apps

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'GreetingApp'
]

#----------------------------------------------------------------------------------------------
#Step 5: Goto Application urls.py

GeetingApp------->rightclick--->newfile------->urls.py

from django.urls import re_path
from GreetingApp import views
urlpatterns=[
          re_path(r'^$',views.input)
]

#----------------------------------------------------------------------------------------------
#Step 6: Goto Project urls.py

from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^www.Greeting.com/',include('GreetingApp.urls')),
    re_path(r'^www.Greeting.com/',include('GreetingApp.urls'))
]

#----------------------------------------------------------------------------------------------
#step 7: views.py

from django.shortcuts import render
import datetime
# Create your views here.
def input(request):
    dt=datetime.datetime.now()
    hour=float(dt.strftime("%H"))
    msg="Hello.....Hyderabad!!!"
    if(hour<=12):
        msg=msg+"Very Good Morning!!!"
    elif(hour<=16.00):
        msg=msg+"Very Good Afternoon!!!"
    elif(hour<=20.00):
        msg=msg+"Very Good Evening!!!"
    else:
        msg=msg+"Very Good Night!!!"
    dict={'message':msg,"date":dt}
    return render(request,'base.html',dict)

#---------------------------------------------------------------------------------------
#step 8: Creating Templates folder

myproj11(outer folder) ------->right click------->new folder ------>"templates"

"templates" ------->New file ------->base.html



<html>
<head>
  <style>
    body {
        background:red;
        color :yellow ;
        }
   </style>
</head>
<body>
<h1> {{message}} </h1>
<h2> The Current Date and Time is :{{date}}</h2>
</body>
</html>
 
#-----------------------------------------------------------------------------------------------
#step 9: Goto settings.py and add templates folder path

import os

TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],

#-----------------------------------------------------------------------------------------------
#sTEP 10:Migrate

(myvenv) C:\djangoapps\myproj11>py manage.py migrate

#----------------------------------------------------------------------------------------------
#step 11: Runserver
(myvenv) C:\djangoapps\myproj11>py manage.py migrate

#---------------------------------------------------------------------------------------------
#Step 12: Giving Request:
http://127.0.0.1:8000/GreetingApp/
or
http://127.0.0.1:8000/www.Greeting.com/

#o/p:
Hello.....Hyderabad!!!..Very Good Morning!!!
The Current Date and Time is :Jan. 22, 2023, 11:04 a.m.

#---------------------------------------------------------------------------------
#we can also specify multiple html files in views.py

#GreetingApp--->rightclick------->newfile--->views1.py

from django.shortcuts import render
import datetime
# Create your views here.
def input(request):
    dt=datetime.datetime.now()
    hour=float(dt.strftime("%H"))
    msg="Hello.....Hyderabad!!!"
    if(hour<12):
        return render(request,'morning.html',{"date":dt})
    elif(hour<16.00):
        return render(request,'afternoon.html',{"date":dt})
    elif(hour<20.00):
        return render(request,'evening.html',{"date":dt)
    return render(request,'night.html',{"date":dt})

#--------------------------------------------------------------------------------------------
#morning.html

<html>
<head>
  <style>
    body {
        background:red;
        color :yellow ;
        }
   </style>
</head>
<body>
<h1>Hello.....Hyderabad...Very Good Morning!!!
<h2> The Current Date and Time is :{{date}}</h2>
</body>
</html>

#-------------------------------------------------------------------------------------------
#afternoon.html

<html>
<head>
  <style>
    body {
        background:red;
        color :yellow ;
        }
   </style>
</head>
<body>
<h1>Hello.....Hyderabad...Very Good Afternoon!!!
<h2> The Current Date and Time is :{{date}}</h2>
</body>
</html>

#---------------------------------------------------------------------------------------
#evening.html

<html>
<head>
  <style>
    body {
        background:red;
        color :yellow ;
        }
   </style>
</head>
<body>
<h1>Hello.....Hyderabad...Very Good Evening!!!
<h2> The Current Date and Time is :{{date}}</h2>
</body>
</html>
#-----------------------------------------------------------------------------------------
#night.html

<html>
<head>
  <style>
    body {
        background:red;
        color :yellow ;
        }
   </style>
</head>
<body>
<h1>Hello.....Hyderabad...Very Good Night!!!
<h2> The Current Date and Time is :{{date}}</h2>
</body>
</html>

          
#--------------------------------------------------------------------------------------------
#Goto Application urls.py

from django.urls import re_path
from . import views
from . import views1
urlpatterns = [
    #re_path(r'^$',views.input),
    re_path(r'^$',views1.input)

#-----------------------------------------------------------------------------
#Give request:

http://127.0.0.1:8000/GreetingApp/

o/p:

Hello.....Hyderabad!!!..Very Good Morning!!!
The Current Date and Time is :Jan. 22, 2023, 11:04 a.m.


















