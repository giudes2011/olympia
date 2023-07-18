from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from olympia import views
def artiList(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articleList.html', {'articles': articles})
def artiDetail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/articleDetail.html', { 'article': article })
@login_required(login_url="/account/login/")
def articleCreateForm(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            saveToDB = form.save(commit=False)
            saveToDB.author = request.user
            saveToDB.save()
            return redirect(views.home)
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/articleCreate.html', { 'form': form })