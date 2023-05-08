from django.shortcuts import render

# Create your views here.


def homeview(req):
    return render(req, 'home.html')