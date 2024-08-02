from django.shortcuts import render

# Create your views here.

def login_register(request):
    if request.method == "POST":
        type_of_btn = request.POST.get('log')
        if type_of_btn == 'login':
            print('login detected')
        if type_of_btn == 'signup':
            print('signup detected')


    return render(request,'login_signup.html')
