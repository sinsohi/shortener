from django.shortcuts import render, redirect
from url.forms import UrlForm
from url.models import URL

# Create your views here.
def get_shortened_url(request, shortened):
   url = URL.objects.filter(shortened__exact=shortened).get()
   
   if url == None:
       return redirect(show_home)
   return redirect(str(url.link))

def show_home(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        url = form.save(commit=False)
        url.shortened = url.link[0:5]
        url.save()
        return render(request, 'url/shorten.html',{"url":url.shortened})
    url_form = UrlForm()
    
    
    return render(request, 'url/index.html',{"form": url_form})