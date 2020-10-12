from django.shortcuts import render

from users.form import FormCreateUser


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    context = {
        'form': FormCreateUser
    }
    return render(
        request,
        'signup.html',
        context
    )

def logout_user(request):
    return render(
        request,
        'logout.html'
    )
