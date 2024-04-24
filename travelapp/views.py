
from django.http import HttpResponse
from django.shortcuts import render
from . models import  place
def home(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})
def about(request):
    return render(request,"about.html")
#def about(request):
    #return render(request,"about.html")
#def contact(request):
   # return render(request,"contact.html")