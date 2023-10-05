from django.shortcuts import render, redirect
from django.contrib.auth import forms, login,authenticate

# Create your views here.
def show_register(request):
    if request.method == "POST":
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(False)
            user.save()
            return render(request, "account/complete.html",{"username":user.username})
    else:
        form = forms.UserCreationForm()
        
    return render(request, "account/register.html",{"form":form})

def show_login(request):
    if request.method == "POST":
        form = forms.AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect("url:index")
            
    else:
        form = forms.AuthenticationForm()
        
    return render(request, "account/register.html",{"form":form})

        