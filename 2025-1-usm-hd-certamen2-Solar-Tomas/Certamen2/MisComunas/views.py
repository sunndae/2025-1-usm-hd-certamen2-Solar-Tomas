from django.shortcuts import render, redirect, get_object_or_404
from .models import Comuna
from .forms import ComunaForm
# Create your views here.


def listarComunas(request):
    comunas = Comuna.objects.all()
    return render(request, 'MisComunas/list.html', {'comunas': comunas})


def comuna_create(request):
    if request.method == 'POST':
        form =  ComunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarComunas')
    else:
        form = ComunaForm()
    return render(request, 'MisComunas/form.html', {'form':form})

def comuna_update(request, pk): 
    comuna = get_object_or_404(Comuna, pk=pk)
    if request.method == 'POST':
        form = ComunaForm(request.POST, instance=comuna)
        if form.is_valid():
            form.save()
            return redirect('listarComunas')
    else:
        form = ComunaForm(instance=comuna)
    return render(request, 'MisComunas/form.html', {'form': form})


def comuna_delete(request, pk): 
    comuna = get_object_or_404(Comuna, pk=pk)
    if request.method == 'POST':
        comuna.delete()
        return redirect('listarComunas')
    return render(request, 'MisComunas/confirm_delete.html', {'comuna': comuna})


