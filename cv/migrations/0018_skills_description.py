# Generated by Django 4.2.6 on 2023-10-15 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0017_remove_jobetudiant_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='description',
            field=models.TextField(default='Description par défaut', max_length=500),
        ),
    ]
