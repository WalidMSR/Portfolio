from django.db import models

# Create your models here.
class Home(models.Model) :
    name = models.CharField(max_length=30)
    #salutaion
    greetings1 = models.CharField(max_length=50) 
    greetings2 = models.CharField(max_length=100)
    #picture = models.ImageField(upload_to='picture_home/')
    
    updated = models.DateTimeField(auto_now=True)
    # save my name as object in interface of administration 
    def __str__(self) : 
        return self.name

class About(models.Model) : 
    name = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    picture  = models.ImageField(upload_to = "picture_profile/")

    updated = models.DateTimeField(auto_now=True)
    def __str__(self) : 
        return self.name     
class Contact(models.Model) : 
    about  = models.ForeignKey(About,on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)

class Education(models.Model) : 
    specialty = models.TextField(max_length=100)
    university = models.TextField(max_length=100)
    academic_year = models.DateField()
    updated = models.DateTimeField(auto_now=True)
    def __str__(self) : 
        return self.specialty 
    
    class Meta:
        verbose_name        = 'Education'
        verbose_name_plural = 'EducationS'

class Skills(models.Model) :
    language = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self) : 
        return self.language 
    class Meta:
        verbose_name        = 'Skill'
        verbose_name_plural = 'Skills'

 
class Project(models.Model) : 
    name_project = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    date  = models.DateField()

    updated = models.DateTimeField(auto_now=True)
    def __str__(self) : 
        return self.name_project 
    
    class Meta:
        verbose_name        = 'Project'
        verbose_name_plural = 'Projects'

class Experience(models.Model) : 
    date  = models.DateField()
    job_name = models.TextField(max_length=100)
    description = models.TextField(max_length=100)

    updated = models.DateTimeField(auto_now=True)
    def __str__(self) : 
        return self.job_name 

class Contact_me(models.Model) : 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=50)
    messgae =models.TextField(max_length=200) 
    updated = models.DateTimeField(auto_now=True)
    def __str__(self) : 
        return f'{self.first_name}{self.last_name}' 
