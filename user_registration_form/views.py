from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from user_registration_form.forms import RegisterForm
from user_registration_form.models import CustomUser, Profile


########################################################
# def home(request):
#     user = request.user  # currently logged-in user
#     return render(request, "home.html", {"user_obj": user})


def home(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        return render(request, "home.html", {"profile": profile})
    return render(request, "home.html")


####################################################
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


################################################################
def login_view(request):
    """
    Login page: authenticate user.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


######################################################################
def logout_view(request):
    """
    Logout user and redirect to home.
    """
    logout(request)
    return redirect("home")
