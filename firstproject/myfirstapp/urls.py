from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
]
def bonjour(request):
    nom=request.GET["nom"] # récupère la valeur du paramètre nom du formulaire
    return render(request,'myfirstapp/bonjour.html',{"nom":nom}) # passe cette valeur à la vue au travers du dictionnaire de contexte