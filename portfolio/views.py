from django.shortcuts import render
from .models import Project

# Create your views here.

def Homepage(request):
    projects = Project.objects.all()
    return render(request,"portfolio/Homepage.html",{"projects":projects})
