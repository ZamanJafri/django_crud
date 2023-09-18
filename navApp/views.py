from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import Member,Img
# Create your views here.

def homePage(request):
    # this query is used select data from database
    # select *from table_name
    data = Member.objects.all()
    return render(request,"index.html",{'data':data})
def aboutPage(request):
    return render(request,"about.html")
def servicesPage(request):
    return render(request,"services.html")
def contactPage(request):
    if request.method == 'POST':
       m = Member()
       m.firstname = request.POST.get('firstname')     
       m.lastname = request.POST.get('lastname')    
       m.save()
       return HttpResponseRedirect('/')
    return render(request,"contact.html")


def deletePage(request,id):
    data = Member.objects.get(id=id)
    if(data):
        data.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
