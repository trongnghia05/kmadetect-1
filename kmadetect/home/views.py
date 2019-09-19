#kmadetect
#By Nguyen Trung

import shutil
import os
from reverse import reverse as rev
from detect import Train
import time


from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView  
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

PATH_TEMP = '../reverse/tempApks'

from django.http import HttpResponse
# Create your views here.
def index(request):
   return render(request, 'pages/home.html')


def upload(request):
   context = {}
   if request.method == 'POST':
      uploaded_file = request.FILES['fileApk']
      fs = FileSystemStorage()
      name = fs.save(uploaded_file.name, uploaded_file)
      print(name)
      context['url'] = fs.path(name)

      # while True:
      #    if os.path.exists(fs.path(name)):
      #       break
      # time.sleep(20)

      # shutil.move(fs.path(name), os.path.join(PATH_TEMP, name))
      nameMd5 = rev.reverse(name)
      if nameMd5 == 'Error':
         labelDetect = 'Null'
      else:
         labelDetect = Train.detectApk(nameMd5)


      if labelDetect == 'Null':
         Mess = 'Cant detect what kind of file'
      else:
         Mess = 'Detected'

      context['labelDetect'] = labelDetect
      context['Mess'] = Mess
   return render(request, 'pages/resuilt.html', context)

