from django.shortcuts import render, redirect, get_object_or_404
from .models import Perro, UsuarioAdoptante, Postulacion
from django.contrib.auth.decorators import login_required

def perros_disponibles(request):
    perros = Perro.objects.filter(estado='disponible')
    return render(request, 'perros/perros_disponibles.html', {'perros': perros})

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