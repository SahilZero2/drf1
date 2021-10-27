from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import employe
from django.core.exceptions import *
from django.views.generic import TemplateView, ListView
# from django.contrib.auth.models import User
from django.db import IntegrityError


# from .filters import UserFilter

# Create your views here.

def index(request):
    return render(request, 'form.html')

def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield' )
        try:
           webpages_list = employe.objects.get(employe_name = search_id)
           data_list = {webpages_list}
            
           return render(request,'index.html', { 'context' : data_list})
        except employe.DoesNotExist:
            return HttpResponse("Their is no record of this employe")
    else:
        return render(request, 'form.html')


def createemploye(request):
    if request.method == 'POST':
        try:
            obj = employe(
                employe_name = request.POST.get('employe_name'),
                salary = request.POST.get('salary'),
                )   
            obj.save()
            return render(request, 'create.html',{'title':'The data has saved succesfully!'})
            # return redirect('index')
        except IntegrityError:
            return render(request,"create.html",{'error':'This user name has already been taken , please chose another one !'})  
        
    else:
        return render(request,"create.html")


