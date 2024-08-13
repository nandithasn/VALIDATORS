from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
from app.forms import *

def create_student(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFO=StudentForm(request.POST)
        if SFO.is_valid():
            sid=SFO.cleaned_data['sid']
            sn=SFO.cleaned_data['sname']
            sage=SFO.cleaned_data['sage']
            semail=SFO.cleaned_data['semail']
            SO=Student.objects.get_or_create(sid=sid,sname=sn,sage=sage,semail=semail)[0]
            SO.save()
            return HttpResponse('student is created')
        else:
            return HttpResponse('invalid data')

    return render(request,'create_student.html',d)