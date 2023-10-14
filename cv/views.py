from django.shortcuts import render
from .models import *
# Create your views here.
def index(request) :
  
    home = Home.objects.latest('updated')
    about = About.objects.latest('updated')
    contact = Contact.objects.filter(about=about)
    # skills = Skills.objects.all()
    # project = Project.objects.all()

    context = {
        'home': home,
        'about': about,
        'contact': contact,
        # 'skills': skills,
        # 'project': project,
   }

    return render(request, 'index.html',context)