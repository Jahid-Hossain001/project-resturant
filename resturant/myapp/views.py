from django.shortcuts import render


# Create your views here.

def home(request):
    
    return render(request, 'index.html')

def user_login(request):
    
    return render(request,'auth/login.html')



