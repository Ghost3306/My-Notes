from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from accounts.models import Profile
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username)
        if not user_obj.exists():
            context = {
                'msg':'User not found!'
            }
            return render(request,'login.html',context)
        try:
            if not user_obj[0].profile.is_verified:
                context = {
                'msg':'Your account is not verified!'
                }
                return render(request,'login.html',context)
        except Exception as e:
            print(e)

        user_obj = authenticate(username=username,password=password)
        if user_obj is not None:
            login(request,user_obj)
            return redirect('/')
        else:
            context = {
            'msg':'Invalid username or password!'
            }
            return render(request,'login.html',context)
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cnpassword = request.POST.get('cnpassword')
        print(username,password,cnpassword)
        if password == cnpassword:
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                context = {
                'msg':'User already exists'
                }
                return render(request,'register.html',context)
            else:
                user_obj = User(email=username,username=username)
                user_obj.set_password(password)
                user_obj.save()
                context = {
                'msg':'Check your email for verification'
                }
                return render(request,'register.html',context)
        else:
            context = {
                'msg':'Confirm password doesn\'t match'
            }
            return render(request,'register.html',context)
    return render(request,'register.html')

def activate_profile(request,uuid):
    
    user_obj = Profile.objects.filter(email_token=uuid)

    if user_obj.exists():
        if user_obj.first().is_verified:
            context = {
                'msg':'Your Profile is already verified!'
            }
            return render(request,'activate_email.html',context)
        else:
            user_obj = Profile.objects.get(email_token=uuid)
            user_obj.is_verified = True
            user_obj.save()
            context = {
                'msg':'Your Profile verified successfully'
            }
            return render(request,'activate_email.html',context)
    context = {
                'msg':'Invalid token!'
            }   
    return render(request,'activate_email.html',context)


def logout_user(request):
    logout(request)
    return redirect('/')