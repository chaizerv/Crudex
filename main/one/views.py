from django.shortcuts import render, redirect
from .forms import CrudexForm
from .models import Crudex

def read(request):
    # Вывод всех объектов из базы
    context = {'read':Crudex.objects.all()}
    return render(request, "one/read.html", context)

def create_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CrudexForm()
        else:
            crud = Crudex.objects.get(pk=id)
            form = CrudexForm(instance=crud)
        return render(request, 'one/create_form.html',{'form':form})
    else:   # Редактирование и сохранение пользователя
        if id == 0:
            form = CrudexForm(request.POST)
        else:
            crud = Crudex.objects.get(pk=id)
            form = CrudexForm(request.POST, instance=crud)
        if form.is_valid():
            form.save()
        return redirect('/read')


def delete(request,id):
    crud = Crudex.objects.get(pk=id)
    crud.delete()
    return redirect('/read')

