from django.shortcuts import render,HttpResponse
from home.models import Contact
def home(request):
    context={'name':'Anurag','topic':'Django'}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        ins = Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print("The entries has been stored inside the database")
    return render(request,'Contact.html')

def project(request):
    # return HttpResponse("This is the Projects page")
    return render(request,'project.html')

