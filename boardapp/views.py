from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.models import User #Djangoが定義しているユーザーモデルを利用する
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import PostModel

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
            return HttpResponse("<p>ログイン成功</p>")
        else:
            return render(request, "login.html", {"login_error":"ログインに失敗しました。"}) 
    
    #始めてきたユーザー(GET)
    else: 
        return render(request, "login.html", {})


def listfunc(request): 
    posts = PostModel.objects.all()
    return render(request, "list.html", {"posts":posts})