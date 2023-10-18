from django.db import models

# Create your models here.
#Home
class Home(models.Model) :
    name = models.CharField(max_length=10)
    #salutaion
    greetings1 = models.CharField(max_length=30)
    greetings2 = models.CharField(max_length=30)
    #picture = models.ImageField(upload_to='picture_home/')
    updated = models.DateTimeField(auto_now=True)
    # save my name as object in interface of administration 
    def __str__(self) : 
        return self.name
#About
class About(models.Model) : 
    name = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    picture  = models.ImageField(upload_to = "picture_profile/")
    # Utilisez FileField pour stocker le fichier PDF
    cv = models.FileField(upload_to="cv_files/", default='False')
    updated = models.DateTimeField(auto_now=True)
    def __str__(self) : 
        return self.name



# Contact
class Contact(models.Model) : 
    about  = models.ForeignKey(About,on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)







#Education
class Education(models.Model) :
    date = models.TextField(max_length=500, default="Date par défaut")
    title = models.CharField(max_length=100, default="titrepar défaut")
    location = models.CharField(max_length=100,default="position par défaut")
    #description = models.TextField(max_length=500, default="Description par défaut")
    en_cours = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name        = 'Education'
        verbose_name_plural = 'EducationS'



#Skills
class Skills(models.Model) :
    picture = models.ImageField(upload_to='picture_Skills/', null=True, blank=True)
    language = models.CharField(max_length=20)
    description = models.TextField(max_length=500, default="Description par défaut")
    updated = models.DateTimeField(auto_now=True)
    def __str__(self) : 
        return self.language

    class Meta:
        verbose_name        = 'Skill'
        verbose_name_plural = 'Skills'



#Project
class Project(models.Model) :
    date = models.TextField(max_length=500, default="Date par défaut")
    name_project = models.CharField(max_length=100, default="nom  par défaut")
    description = models.TextField(max_length=1000, default="Description par défaut")
    en_cours = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self) : 
        return self.name_project 
    
    class Meta:
        verbose_name        = 'Project'
        verbose_name_plural = 'Projects'

#Experience
class ExperienceProfessionnelle(models.Model):
    date = models.TextField(max_length=500, default="Description par défaut")
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title
class JobEtudiant(models.Model):
    date = models.TextField(max_length=500, default="Description par défaut")
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.title
#Contact_me
class Contact_me(models.Model) : 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=50)
    messgae =models.TextField(max_length=200) 
    updated = models.DateTimeField(auto_now=True)
    def __str__(self) : 
        return f'{self.first_name}{self.last_name}' 
