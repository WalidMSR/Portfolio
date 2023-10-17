# Generated by Django 4.2.6 on 2023-10-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0012_experienceprofessionnelle_jobetudiant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='en_cours',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.TextField(default='Description par défaut', max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default='Description par défaut', max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='name_project',
            field=models.CharField(default='Description par défaut', max_length=100),
        ),
    ]
