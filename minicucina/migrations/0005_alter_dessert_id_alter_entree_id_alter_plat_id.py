# Generated by Django 4.2.2 on 2023-07-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minicucina', '0004_alter_dessert_id_alter_entree_id_alter_plat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessert',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='entree',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='plat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
