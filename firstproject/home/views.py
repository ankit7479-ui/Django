from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'variable1': 'Harry is Great',
        'variable2': 'Harsh Bhaiya is Great Person'
    }
    return render(request,'index.html',context)
    #return HttpResponse("This is Home page ")

def about(request):
    return render(request,'about.html')
   

def services(request):
    return render(request,'services.html')
   

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = contact(name=name,Email=Email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your Profile has been sent')
    return render(request,'contact.html')

   
