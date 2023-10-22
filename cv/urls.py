from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path('download_report/<int:project_id>/', views.download_report, name='download_report'),
]
