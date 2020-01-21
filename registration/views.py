from django.shortcuts import render
from . import form


# Create your views here.


def enter(request):
    context = {"form1": form.User}
    return render(request, "index.html", context)


