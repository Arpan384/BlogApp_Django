from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()   #returns the saved user implicitly
            #log the user in
            login(req,user)
            return redirect('articles:list')  #redirect to articles
    elif req.method == "GET":
        form = UserCreationForm()
    return render(req,"accounts/signup.html", {"form":form})


def login_view(req):
    if req.method == "POST":
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            #login the user
            user = form.get_user()
            login(req,user)
            # print("call1  ", req.POST.get('next'))
            if 'next' in req.POST:
                # print("call")
                return redirect(req.POST.get('next'))
            else:
                return redirect('articles:list')  #redirect to articles
    elif req.method == "GET":
        form = AuthenticationForm()
    return render(req, "accounts/login.html", {"form":form})


def logout_view(req):
    if req.method=="POST":
        logout(req)
        return redirect("articles:list")