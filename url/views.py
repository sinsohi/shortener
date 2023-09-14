from django.shortcuts import render

# Create your views here.
def get_shortened_url(request, url):
    if url == "naver":
        result = "https://www.daum.net/"
    else:
        result = "Not Found"
    return render(request, 'index.html',{"url":result})

def show_home(request):
    
    return render(request, 'url/index.html')