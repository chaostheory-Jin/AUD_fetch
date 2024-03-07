from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hi")

def dumpData(request):
    data = request.GET
    resinfo = {"isok":True}
    
    return HttpResponse(resinfo)