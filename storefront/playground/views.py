from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def stepInto () :
    return "stepped into the current function"

def say_hello (request):
    first = "add the first break point here"
    nextLine = "observe the code is executed line by line when step over is clicked on the top debug tool bar"
    lineStepInto = stepInto ()
    return render (request, "hello.html", { "name" : "CY" })