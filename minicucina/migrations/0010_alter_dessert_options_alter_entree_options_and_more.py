# Generated by Django 4.2.2 on 2023-07-25 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minicucina', '0009_alter_dessert_options_alter_entree_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dessert',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='entree',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='plat',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='dessert',
            name='order',
        ),
        migrations.RemoveField(
            model_name='entree',
            name='order',
        ),
        migrations.RemoveField(
            model_name='plat',
            name='order',
        ),
    ]
