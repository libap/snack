# Generated by Django 4.2.2 on 2023-07-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minicucina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plat',
            name='image',
            field=models.ImageField(upload_to='minicucina/images/plats/'),
        ),
    ]