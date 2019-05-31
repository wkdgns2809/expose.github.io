from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('first')
        else:
            return render(request, 'login.html', {'error': '뭔가 틀렷어용'})
    else:
        return render(request, 'login.html')
def signup(request):
    if request.method == 'POST':
        if request.POST['Password'] == request.POST['PasswordConfirm']:
            user = User.objects.create_user(request.POST['id'], password=request.POST['Password'])
            user.profile.nickname = request.POST['nickname']
            user.profile.region = request.POST['region']
            auth.login(request, user)
            return redirect('first')
    return render(request,'signup.html')

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        return redirect('first')
    return render(request,'singup.html')


