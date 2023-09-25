from django.shortcuts import render
from .models import Plat, Entree, Dessert, Boisson
from datetime import datetime
import locale


def home(request):
    # seed_data()  # Appeler la fonction pour générer les données (à appeler une seule fois)

    entrees = Entree.objects.all()
    plats = Plat.objects.all()
    desserts = Dessert.objects.all()
    boissons = Boisson.objects.all()

    jours_semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
    classes = {
        'entrees': entrees,
        'plats': plats,
        'desserts': desserts,
        'boissons': boissons,
        # Ajoutez d'autres classes au besoin
    }

    # Définir la locale française
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

    # Obtenir le jour actuel en français pour l'affichage
    current_day = datetime.now().strftime('%A')

    return render(request, 'minicucina/index.html', {'entrees': entrees, 'plats': plats, 'desserts': desserts, 'boissons': boissons, 'current_day': current_day, 'jours_semaine': jours_semaine, 'classes': classes})


def seed_data():
    # Supprimer toutes les données existantes
    Entree.objects.all().delete()
    Plat.objects.all().delete()
    Dessert.objects.all().delete()

    # Générer les données de l'exemple
    Entree.objects.create(
        nom='Salade de calamars',
        image='static/minicucina/images/entrees/salade_calamar.jpg',
        nom_fichier='salade_calamar.jpg',
        jour='lundi',
        prix=7.95,
        description='Entrée à base de calamars'
    )

    Plat.objects.create(
        nom='Polpettes',
        image='static/minicucina/images/plats/polpette.jpg',
        nom_fichier='plats/polpette.jpg',
        jour='mardi',
        prix=9.99,
        description='Plats pour les carnivores'
    )

    Plat.objects.create(
        nom='Aubergine',
        image='static/minicucina/images/plats/aubergines_parmigiana.jpg',
        nom_fichier='aubergines_parmigiana.jpg',
        jour='mercredi',
        prix=8.50,
        description='De bons légumes bio'
    )

    Plat.objects.create(
        nom='Bucco de veau',
        image='static/minicucina/images/plats/bucco_veau.jpg',
        nom_fichier='bucco_veau.jpg',
        jour='jeudi',
        prix=7.95,
        description='Plat à base de veau'
    )

    Dessert.objects.create(
        nom='Tartelettes à la fraise',
        image='static/minicucina/images/desserts/tartelettes_fraise_frangipane.jpg',
        nom_fichier='tartelettes_fraise_frangipane.jpg',
        jour='vendredi',
        prix=7.95,
        description='Dessert à la fraise'
    )
