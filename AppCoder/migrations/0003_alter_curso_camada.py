# Generated by Django 4.2.7 on 2023-11-22 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_entregable_profesor_alter_curso_camada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='camada',
            field=models.IntegerField(),
        ),
    ]
