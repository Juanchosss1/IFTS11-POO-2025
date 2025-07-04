# Generated by Django 5.2.2 on 2025-06-18 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0004_alter_perro_estado_salud'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarioadoptante',
            name='preferencia_mascota',
        ),
        migrations.AddField(
            model_name='usuarioadoptante',
            name='pref_edad',
            field=models.CharField(choices=[('cachorro', 'Cachorro'), ('joven', 'Joven'), ('adulto', 'Adulto'), ('indistinto', 'Indistinto')], default='cachorro', max_length=20),
        ),
        migrations.AddField(
            model_name='usuarioadoptante',
            name='pref_estado_salud',
            field=models.CharField(choices=[('saludable', 'Saludable'), ('herido', 'Herido'), ('enfermo', 'Enfermo'), ('enlasultimas', 'En las últimas'), ('recuperado', 'Recuperado')], default='saludable', max_length=20),
        ),
        migrations.AddField(
            model_name='usuarioadoptante',
            name='pref_raza',
            field=models.CharField(choices=[('labrador', 'Labrador'), ('caniche', 'Caniche'), ('bulldog', 'Bulldog'), ('ovejero', 'Ovejero'), ('otro', 'Otro')], default='otro', max_length=20),
        ),
        migrations.AddField(
            model_name='usuarioadoptante',
            name='pref_tamaño',
            field=models.CharField(choices=[('chico', 'Chico'), ('mediano', 'Mediano'), ('grande', 'Grande'), ('gigante', 'Gigante')], default='chico', max_length=20),
        ),
        migrations.AlterField(
            model_name='perro',
            name='edad',
            field=models.CharField(choices=[('cachorro', 'Cachorro'), ('joven', 'Joven'), ('adulto', 'Adulto'), ('indistinto', 'Indistinto')], default='cachorro', max_length=20),
        ),
        migrations.AlterField(
            model_name='perro',
            name='tamaño',
            field=models.CharField(choices=[('chico', 'Chico'), ('mediano', 'Mediano'), ('grande', 'Grande'), ('gigante', 'Gigante')], default='chico', max_length=20),
        ),
    ]
