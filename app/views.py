from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
def d1(request):
    return render(request,'home.html')

def ins(request):
    
    if request.method=='POST':
        id=request.POST['id']
        name=request.POST['name']
        email=request.POST['email']
        salary=request.POST['salary']      
        # TTO=Inse.objects.get_or_create(id=id,name=name,email=email,salary=salary)
        if Inse.objects.filter(id=id).exists():
            return HttpResponse('''<h1>Employee already there /\ use Update the details</h1> ''')
        else:
            dd=Inse.objects.create(id=id, name=name, email=email,salary=salary)
            return HttpResponse(f'<h1 class="text-danger">employee data has inserted:{id,name}</h1>')
         
    return render(request,'ins.html')

def upda(request):
    ot=Inse.objects.all()
    d={'ot':ot}
    if request.method=='POST':
        id=request.POST['id']
        name=request.POST['name']
        email=request.POST['email']
        salary=request.POST['salary'] 
        if  Inse.objects.filter(id=id).update(name=name,email=email,salary=salary):
            pass
        return render(request,'upda.html',d)
    
    return render(request,'upda.html')
    
def del1(request):
    ot=Inse.objects.all()
    d={'ot':ot}
    if request.method=='POST':
        id=request.POST['id']
        Inse.objects.filter(id=id).delete()
        return HttpResponse('employee data is deleted..')
        #return render(request,'delete.html',d)
  
    return render(request,'del1.html')