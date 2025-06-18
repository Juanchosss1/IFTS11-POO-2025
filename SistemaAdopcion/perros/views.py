from django.shortcuts import render, redirect, get_object_or_404
from .services.sistema_adopcion_service import SistemaAdopcion
from .models import Perro, UsuarioAdoptante, Postulacion
from django.contrib.auth.decorators import login_required

def perros_disponibles(request):
    perros = Perro.objects.filter(estado_adopcion='disponible')
    return render(request, 'perros/perros_disponibles.html', {'perros': perros})

@login_required
def panel_adopcion(request):
    sistema = SistemaAdopcion()
    sistema.perros = list(Perro.objects.all())
    sistema.usuarios = list(UsuarioAdoptante.objects.all())

    try:
        usuario = UsuarioAdoptante.objects.get(user=request.user)
    except UsuarioAdoptante.DoesNotExist:
        usuario = None

    sugeridos = sistema.sugerir_perros(usuario) if usuario else []
    perros_disponibles = sistema.perros

    return render(request, 'perros/panel_adopcion.html', {
        'sugeridos': sugeridos,
        'perros_disponibles': perros_disponibles,
        'usuario': usuario,
    })

@login_required
def postular_perro(request, perro_id):
    perro = get_object_or_404(Perro, id=perro_id)
    usuario = UsuarioAdoptante.objects.get(user=request.user)
    Postulacion.objects.create(usuario=usuario, perro=perro)
    return redirect('perros_disponibles')

@login_required
def confirmar_adopcion(request, postulacion_id):
    postulacion = get_object_or_404(Postulacion, id=postulacion_id)
    postulacion.confirmada = True
    postulacion.perro.estado = 'adoptado'
    postulacion.perro.save()
    postulacion.save()
    return redirect('mis_postulaciones')

@login_required
def mis_postulaciones(request):
    usuario = UsuarioAdoptante.objects.get(user=request.user)
    postulaciones = Postulacion.objects.filter(usuario=usuario)
    return render(request, 'perros/mis_postulaciones.html', {'postulaciones': postulaciones})

def sugerencias_perros(request):
    sistema = SistemaAdopcion()
    # Carga los perros y usuarios desde la base de datos
    sistema.perros = list(Perro.objects.all())
    usuario = UsuarioAdoptante.objects.get(user=request.user)
    sistema.usuarios = [usuario]
    sugeridos = sistema.sugerir_perros(usuario)
    return render(request, 'perros/sugerencias.html', {'perros': sugeridos})