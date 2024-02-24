from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .form import ForgetPasswordForm, ChangePasswordForm, LoginForm

def login_user(request):
    data={}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form_inputs = form.clean_data()
            phone_number = form_inputs.get('phone_number')
            password = form_inputs.get('password')
            user = authenticate(request=request, username=phone_number, password=password)
            if user:
                user_groups  = user.groups.all()
                is_user =  bool(user_groups.filter(name="user"))
                request.session['is_user'] = is_user
            
    else:
        data['form'] = LoginForm()
    
    return render(request=request, template_name="login.html", context=data)

@login_required(login_url=settings.LOGIN_URL)
def reset_password(request):
    data = {}
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            form_inputs = form.clean_data()
            old_password = form_inputs.get('old_password')
            new_password = form_inputs.get('new_password')
            user = authenticate(request=request, username=request.user.username, password=old_password)
            if user:
                user.set_password(new_password)
                user.save()
                return redirect('accounts:profil')
        data['form'] = form
        return redirect('accounts:profil')

@login_required(login_url=settings.LOGIN_URL)
def forget_password(request):
    data = {}
    if request.POST:
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email_or_phone_number = form.clean_data().get('email_or_phone_number')
            try:
                user = User.objects.get(email=email_or_phone_number)
            except:
                user = None
            if not user:
                try:
                    user = User.objects.filter(username=email_or_phone_number)
                except:
                    user = None
            if user:
                is_already_use = True
                new_random_password = User.objects.make_random_password()
                while is_already_use:
                    try:
                        user.set_password(new_random_password)
                        is_already_use = False
                    except:
                        new_random_password = User.objects.make_random_password()
                # send sms or mail with new_random_password
                return redirect('accounts:login')
        data['form'] = form
    else:
        data['form'] = ForgetPasswordForm()
    return render(request=request, template_name='forget_password', context=data)

@login_required(login_url=settings.LOGIN_URL)
def logout_user(request):
    logout(request=request)
    return redirect("accounts:login")    

