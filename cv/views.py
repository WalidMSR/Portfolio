from django.shortcuts import render
from .models import *
# Create your views here.
def index(request) :
  
    home = Home.objects.latest('updated')
    about = About.objects.latest('updated')
    contact = Contact.objects.filter(about=about)
    educations = Education.objects.all()
    experiences = ExperienceProfessionnelle.objects.all()
    jobs = JobEtudiant.objects.all()
    projects = Project.objects.all()
    skills = Skills.objects.all()


    context = {
        'home': home,
        'about': about,
        'contact': contact,
        'educations': educations,
        'experiences': experiences,
        'jobs': jobs,
        'projects': projects,
        'skills': skills,

   }

    return render(request, 'index.html',context)