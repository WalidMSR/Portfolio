from django.contrib import admin
from .models import Home, About, Education, ExperienceProfessionnelle, Skills, Contact_me, Project, Contact, JobEtudiant

# Register your models here.
admin.site.register(Home)

#admin.site.register(About)
class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1



@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ContactInline,
    ]



admin.site.register(Education)
admin.site.register(ExperienceProfessionnelle)
admin.site.register(JobEtudiant)



admin.site.register(Skills)
class skillsinline(admin.TabularInline) : 
    model = Skills
    extra = 1



admin.site.register(Contact_me)

admin.site.register(Project)





