from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# @login_required(login_url="login/")  #setting home view

def home(request):
    print "testing"
    return render(request,"home.html")
