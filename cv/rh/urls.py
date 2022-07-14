from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("employment", views.employment, name="employment"),
    path("experience", views.experience, name="experience"),
    path("projects", views.projects, name="projects"),
    path("indice", views.indice, name="indice"),
    path("empleo", views.empleo, name="empleo"),
    path("experiencia", views.experiencia, name="experiencia"),
    path("obras", views.obras, name="obras"),
]
