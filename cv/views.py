from django.shortcuts import render, HttpResponseRedirect
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
    #visitors = Contact_me.objects.all()

    #confirmation_message = ""  # Message de confirmation initial vide
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mail = request.POST.get('mail')
        message = request.POST.get('message')

        Contact_me.objects.create(
            first_name=first_name,
            last_name=last_name,
            mail=mail,
            message=message
        )
    #   confirmation_message = "Merci pour votre message. Nous vous répondrons bientôt."



    context = {
        'home': home,
        'about': about,
        'contact': contact,
        'educations': educations,
        'experiences': experiences,
        'jobs': jobs,
        'projects': projects,
        'skills': skills,
        #'visitors': visitors
        #
    }
    return render(request, 'index.html',context)
