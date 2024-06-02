from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view means request -> response
# request handler
# action

def say_hello(request):
    # pull ddata from db
    # transform
    # send email
    # return HttpResponse('hello world')
    return render(request, 'hello.html', {'name': 'Asib'})