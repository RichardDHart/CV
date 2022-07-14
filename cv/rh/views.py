from django.shortcuts import render

def index(request):
    return render(request, "rh/index.html")
def employment(request):
    return render(request, "rh/employment.html")
def experience(request):
    return render(request, "rh/experience.html")
def projects(request):
    return render(request, "rh/projects.html")
def indice(request):
    return render(request, "rh/indice.html")
def empleo(request):
    return render(request, "rh/empleo.html")
def experiencia(request):
    return render(request, "rh/experiencia.html")
def obras(request):
    return render(request, "rh/obras.html")


