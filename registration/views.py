from django.shortcuts import render,redirect,reverse
from django.views.decorators.http import require_GET,require_POST
from . import form
from django.contrib.auth import login, authenticate
from .models import User


@require_GET
def enter(request):
    context = {"form1": form.UserForm, "form2": form.SignInForm}
    return render(request, "index.html", context)


@require_POST
def signin(request):
    myform = form.SignInForm(request.POST)
    print(request.POST.get('username'))
    if myform.is_valid():
        data = myform.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            return redirect(reverse("gallery:home"))
        else:
            return redirect(reverse("register:index"))

    return redirect(reverse("register:index"))


@require_POST
def signup(request):
    myform = form.UserForm(request.POST)
    if myform.is_valid():
        data = myform.cleaned_data
        user = User()
        user.username = data['username']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.birth_date = data['birth_date']
        user.bio = data['bio']
        user.set_password(data['password'])
        user.save()
        user = authenticate(username=data['username'], password=data['password'])
        login(request, user)
        return redirect(reverse("gallery:home"))
    print(1)
    return redirect(reverse("register:index"))




