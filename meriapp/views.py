from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import  Emailspam
from .forms import contact_form
from django.core.mail import send_mail

# Create your views here.
def index(request):
   emailspam= Emailspam.objects.all()
   print(emailspam)
   return render(request,'index.html',{'emailspams':emailspam})

def register(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        username=request.POST.get('uname')
    
        if User.objects.filter(email=email).exists():
          messages.warning(request,'email is already exits')
          return redirect('register')
        else: 
          user=User(email=email,password=password,first_name=firstname,last_name=lastname,username=username)
          user.set_password(password)
          user.save()
          subject='About registration'
          message= 'Hi {uname}, You have been registered succesfully.'
          email_from='rachita.basnet09@gmail.com'
          rec_list=[email,]
          send_mail(subject,message,email_from,rec_list)
          messages.success(request, 'user has been registered successfully')
          return redirect('login')
    return render(request,'register.html')
def login_user(request):
  if request.method=='POST':
     username = request.POST['uname']
     password = request.POST['password']
     print(username)
     user = authenticate(request, username=username, password=password)
     if user is not None:
        login(request, user)
        return redirect('/')
        
     else:
        messages.warning(request,'Invalid Credentials')
        return redirect('login')
  return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')
def emailspampost(request):
    if request.method=='POST':
       title=request.POST.get('title')
       content=request.POST.get('content')
       print(title,content)
       emailspam= Emailspam(title=title,content=content,user_id=request.user)
       emailspam.save()
       messages.success(request,'post has been submitteed succcesfullly')
       return redirect('/')
      
    return render(request,'emailspam_post.html')
def emailspam_detail(request,id):
  emailspam=Emailspam.objects.get(id=id)
  return render(request,'emailspam_detail.html',{'emailspam':emailspam})

def Contact_form(request):
   form=contact_form()
   if request.method=='POST':
      form=contact_form(request.POST)
      if form.is_valid():
        form.save()
        messages.success(request,'thankyou for your feedback')
        return redirect('/')
   return render(request,'contact_form.html',{'form':form})
  