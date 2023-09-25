# Generated by Django 4.2.2 on 2023-07-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minicucina', '0007_dessert_nom_fichier_alter_dessert_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entree',
            name='nom_fichier',
            field=models.CharField(blank=True, editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name='plat',
            name='nom_fichier',
            field=models.CharField(blank=True, editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='dessert',
            name='image',
            field=models.ImageField(upload_to='minicucina/static/minicucina/images/desserts/'),
        ),
        migrations.AlterField(
            model_name='entree',
            name='image',
            field=models.ImageField(upload_to='minicucina/static/minicucina/images/entrees/'),
        ),
        migrations.AlterField(
            model_name='plat',
            name='image',
            field=models.ImageField(upload_to='minicucina/static/minicucina/images/plats/'),
        ),
    ]
