from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm,UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings 
from userauths.models import User

#User = settings.AUTH_USER_MODEL

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Hello {username}, your account was created successfully!")
            new_user = authenticate(username = form.cleaned_data['email'],
                                    password = form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("core:index")
    else:
        form = UserRegisterForm() 
    context = {
        'form' : form, 
    }
    return render(request,"userauths/sign-up.html", context)


"""def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    
    form = UserLoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")

            try:
                user = User.objects.get(email=email)
            except:
                messages.warning(request, f"User with the email {email} does not exist!")
            
           ## if not user.check_password(password):
             ##   messages.error(request, "Incorrect password. Please try again.")
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in!")
                return redirect("core:index")
            else:
                messages.warning(request, "Invalid credentials. Please try again.")
    
    context = {"form": form}
    return render(request, "userauths/sign-in.html", context)"""


def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    
    form = UserLoginForm(request.POST or None)

    if request.method == "POST":
        #form = UserLoginForm
        email = request.POST.get("email")
        password = request.POST.get("password") 

        try:
            user = User.objects.get(email= email)
            user = authenticate(request, email=email, password = password)

            if user is not None:
                login(request,user)
                messages.success(request,"You are logged in!")
                return redirect("core:index")
            else:
                messages.warning(request, "Wrong Password! try again! :)") 
        except:
            messages.warning(request, f"User with email {email} does not exist!")

        
    context = {"form": form}
    return render(request, "userauths/sign-in.html",context)


def logout_view(request):
    logout(request)
    messages.success(request, "You logged out!") 
    return redirect("userauths:sign-in")
