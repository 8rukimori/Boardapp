from django.shortcuts import render, redirect
from django.contrib.auth.models import User #Djangoが定義しているユーザーモデルを利用する
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import PostModel
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def signupfunc(request):

    #POSTメソッドの場合（ユーザーが情報を送信した場合）
    if request.method == "POST":
        username = request.POST["username"] #基本的にはDjangoのフォームを使うべきだが、今回はこれで。
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, "", password)
            return redirect("login")
        except IntegrityError:
            return render(request, "signup.html", {"user_dup":"このユーザーは既に登録されています。"})
    else:
        return render(request, "signup.html", {}) #renderは引数３つ：request(固定)、テンプレート、{モデルデータ}

def loginfunc(request):
    #ログインアクション後のユーザー（POST）
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("list")
        else:
            return render(request, "login.html", {"login_error":"ログインに失敗しました。"}) 
    
    #始めてきたユーザー(GET)
    else: 
        return render(request, "login.html", {})

@login_required
def listfunc(request): 
    posts = PostModel.objects.all()
    return render(request, "list.html", {"posts":posts})

def logout_view(request):
    logout(request)
    return redirect("login")

def detailfunc(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    # post = PostModel.objects.get(pk=pk)
    return render(request, "detail.html", {"post":post})

def likefunc(request, pk):
    post = PostModel.objects.get(pk=pk)
    post.like += 1
    post.save()
    return redirect("list")

def readfunc(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    username = request.user.get_username()
    if username in post.readtxt:
        return redirect("list")
    else: 
        post.read += 1
        post.readtxt = post.readtxt + ' ' + username
        post.save()
        return redirect("list")

class BoardCreate(CreateView):
    template_name = "create.html"
    model = PostModel
    fields = ["title", "content", "post_image", "author"]
    success_url = reverse_lazy("list")

