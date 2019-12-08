from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, "articles/article_list.html", {"arts":articles})

def article_details(req,slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(req, "articles/article_details.html", {"article":article})


@login_required(login_url="/accounts/login/")   #no user can go to article create page if not logged in else user is redirected to specified login page
def article_create(req):
    if req.method == "POST":
        form = forms.CreateArticle(req.POST, req.FILES)
        if form.is_valid():
            #save article to DB
            instance = form.save(commit=False)
            instance.author = req.user
            instance.save()
            return redirect("articles:list")
    else:
        form = forms.CreateArticle()
    return render(req, "articles/article_create.html", {"form":form})