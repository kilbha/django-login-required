from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def HomeView(request):
    return render(request,'MyTemp/home.html')
@login_required
def AddView(request):
    return render(request,'MyTemp/addprod.html')