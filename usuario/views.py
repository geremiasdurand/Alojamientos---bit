from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.user.is_authenticated:
        return redirect("/user_already_logged")
    else:
        if response.method == "POST":
            form = RegisterForm(response.POST)
            if form.is_valid():
                form.save()
            return redirect("/redirect_register_done")
        else:
            form = RegisterForm()

        return render(response, "usuario/register.html", {"form":form})
