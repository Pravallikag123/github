
#Greeting based on current time -GreetingApp

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'GreetingApp'
]

from django.urls import re_path
from GreetingApp import views
urlpatterns=[
          re_path(r'^$',views.input)
]


from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^www.Greeting.com/',include('GreetingApp.urls')),
    re_path(r'^www.Greeting.com/',include('GreetingApp.urls'))
]


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

          
from django.urls import re_path
from . import views
from . import views1
urlpatterns = [
    #re_path(r'^$',views.input),
    re_path(r'^$',views1.input)





















