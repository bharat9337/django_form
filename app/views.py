from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from app.forms import *

def djforms(request):
    ENFO=Nameform()
    d={'ENFO':ENFO}

    if request.method=='POST':
        NFDO=Nameform(request.POST)
        if NFDO.is_valid():
            return HttpResponse(NFDO.cleaned_data)
        else:
            return HttpResponse('Data is not valid')
    return render(request,'djforms.html',d)
