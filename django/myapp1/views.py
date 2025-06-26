from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Index")
    return render(request,"index.html",{"title":"home"})
def about(request):
    return render(request,"about.html",{"title":"about"})

def contact(request):
    return render(request,"contact.html",{"title":"contact"})

def service(request):
    return render(request,"service.html",{"title":"service"})