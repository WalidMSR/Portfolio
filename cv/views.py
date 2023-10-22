from django.http import HttpResponse
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
def download_report(request, project_id):
    project = Project.objects.get(id=project_id)

    if project.pdf_report:
        # Retrieve the PDF file and return it as an attachment
        pdf_file = project.pdf_report.path
        with open(pdf_file, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{project.name_project}_report.pdf"'
            return response

    return HttpResponse('Le rapport de stage n\'est pas disponible.')

def view_report(request, project_id):
    project = Project.objects.get(id=project_id)

    if project.pdf_report:
        # Retrieve the PDF file and return it for viewing in the browser
        pdf_file = project.pdf_report.path
        with open(pdf_file, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            return response

    return HttpResponse('Le rapport de stage n\'est pas disponible.')
