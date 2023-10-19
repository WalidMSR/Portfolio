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

    if request.method == 'POST':
        # Récupérez les données du formulaire
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mail = request.POST.get('mail')
        message = request.POST.get('message')

        # Créez une instance du modèle Contact_me et enregistrez les données dans la base de données
        contact = Contact_me(
            first_name=first_name,
            last_name=last_name,
            mail=mail,
            message=message
        )
        contact.save()
      
  
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
