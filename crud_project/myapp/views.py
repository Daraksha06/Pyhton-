from django.shortcuts import render
from myapp.models import * #import models
# Create your views here.
def index(request):
    return render(request, "index.html")
def reg(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')
        st = Student.objects.create(name= name , email = email , phone = phone , age = age)
        if st:
            return render(request,'index.html', {"msg" : "Registration successful !!"} )
    return render(request, 'index.html')