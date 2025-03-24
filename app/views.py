from django.shortcuts import render, redirect
from .models import *
from random import randint

def SignupPage(request):
    return render(request, "app/signup.html")

def Indexpage(request):
    return render(request, "app/index.html")

def RegisterUser(request):
    if request.method == "POST":
        role = request.POST.get('role', '')

        if role == 'candidate':
            fname = request.POST.get('firstName', '')
            lname = request.POST.get('lastName', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            cpassword = request.POST.get('CPassword', '')

            if UserMaster.objects.filter(email=email).exists():
                message = "User already exists!"
                return render(request, "app/signup.html", {'msg': message})
            else:
                if password == cpassword:
                    otp = randint(100000, 999999)
                    newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=password)
                    newcand = Candidate.objects.create( user_id=newuser,firstname=fname,lastname=lname)
                    return render(request,"app/otpverify.html",{'email':email}) 
                    

        else:
            print("company registration")           


def OTPPage(request):
    return render(request,"app/otpverify.html")

def Otpverify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])
    
    user = UserMaster.objects.get(email=email)
    
    if user:
        if user.otp == otp:
            message = "otp verify successfully"
            return render(request,"app/login.html",{'msg':message})
        else:
            message = "otp is incorrect"
            return render(request,"app/otpverify.html",{'msg':message})
        
    else:
        return render(request,"app/signup.html")    