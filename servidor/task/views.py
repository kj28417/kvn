from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import TaskForm
from .models import Task


def home(request):
    return render(request, "home.html")


def tareas(request):
    tareas = Task.objects.filter(usuario=request.user)
    return render(request, "tareas.html", {
        "tareas": tareas
        })


def registro(request):
    if request.method == "GET":
        return render(request, "singup.html", {
            "formulario": UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                Usuario = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                Usuario.save()
                login(request, Usuario)
                return redirect("tareas")
            except:
                return render(request, "singup.html", {
                    "formulario": UserCreationForm,
                    "error": "El usuario ya existe"
                })
        return render(request, "singup.html", {
            "formulario": UserCreationForm,
            "error": "Contraseña invalida"
        })


def cerrarSesion(request):
    logout(request)
    return redirect("/")


def iniciarSesion(request):
    if request.method == "GET":
        return render(request, "singin.html", {
            "form": AuthenticationForm
        })
    else:
        Usuario = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if Usuario is None:
            return render(request, "singin.html", {
                "form": AuthenticationForm,
                "error": "La contraseña y el usuario no coinsiden"
            })
        else:
            login(request, Usuario)
            return redirect("tareas")


def crearTarea(request):
    if request.method == "GET":
        return render(request, "crear_tarea.html", {
            "form": TaskForm
        })
    else:
        form = TaskForm(request.POST)
        nuevaTarea = form.save(commit=False)
        nuevaTarea.usuario = request.user
        nuevaTarea.save()
        return redirect("tareas")

def detalles(request, tarea_id):
    detallesTarea = get_object_or_404(Task, pk=tarea_id)
    return render(request, "detalles_de_tareas.html", {
        "tarea": detallesTarea
        })