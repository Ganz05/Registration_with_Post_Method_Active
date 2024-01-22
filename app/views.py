from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.

def register(request):
    EUFO=userForm()
    EPFO=profileForm()
    d={'EUFO':EUFO,'EPFO':EPFO}
    if request.method=="POST" and request.FILES:
        CUFO=userForm(request.POST)
        CPFO=profileForm(request.POST,request.FILES)
        if CUFO.is_valid() and CPFO.is_valid():
            MCUFO=CUFO.save(commit=False)
            pw=CUFO.cleaned_data['password']
            MCUFO.set_password(pw)
            MCUFO.save()

            MCPFO=CPFO.save(commit=False)
            MCPFO.username=MCUFO
            MCPFO.save()
            return HttpResponse('Registration SuccussFull')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'register.html',d)
