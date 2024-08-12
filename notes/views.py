from django.shortcuts import render,redirect

# Create your views here.
def homepage(request):
    print(request.user)
    if str(request.user) == 'AnonymousUser':
        return redirect('accounts/login')
    print(request.user.profile.last_seen)
    return render(request,'homepage.html')  