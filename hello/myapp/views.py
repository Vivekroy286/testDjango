from django.shortcuts import render , HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('This is about page')

def services(request):
    return HttpResponse('This is about services')

def contact(request):
    return HttpResponse('1234-5678')