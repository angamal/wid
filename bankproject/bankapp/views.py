from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from bankapp.models import UserAccount


# Create your views here.
def base(request):
    return render(request,'base.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            request.session['logged_in_username'] = user.username
            return redirect('main')
        else:
            pass
    return  render(request,'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create_user(username=username,password=password)
            user.save()
            return redirect('login')
        else:
            pass
    return  render(request,'register.html')

def main_page(request):
    return  render(request,  'main_page.html')

def branches_page(request):
    return render(request, 'branches.html')
#def form_page(request):
    #return render(request, 'form_page.html')
def form_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender=request.POST.get('gender')
        phone_number=request.POST.get('phone_number')
        mail_id=request.POST.get('mail_id')
        address=request.POST.get('address')
        district=request.POST.get('district')
        branch=request.POST.get('branch')
        account_type=request.POST.get('account_type')
        materials=request.POST.getlist('materials')

        user_account=UserAccount(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            mail_id=mail_id,
            address=address,
            district=district,
            branch=branch,
            account_type=account_type,
            materials=materials

        )
        user_account.save()
        message = "Application submitted successfully !"
        return render(request, 'application-success.html',{'message':message})
    return render(request, 'form_page.html',{'home_link':True})
def application_page(request):
    return render(request,'application-success.html')

def logout_view(request):
    logout(request)
    return render(request, 'base.html', {'user': None})