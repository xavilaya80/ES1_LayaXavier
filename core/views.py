"""Unica vista de ReservaGol."""

from django.shortcuts import render

from solucion import cargar_registros, guardar_registro


def resumen(request):
    resultado = None
    error = None

    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        hora_texto = request.POST.get("hora", "").strip()
        jugadores_texto = request.POST.get("jugadores", "").strip()

        try:
            hora = int(hora_texto)
            jugadores = int(jugadores_texto)
            resultado = guardar_registro(nombre, hora, jugadores)
        except ValueError:
            error = "Dato invalido: hora y jugadores deben ser numeros enteros."

    contexto = {
        "resultado": resultado,
        "error": error,
        "registros": cargar_registros(),
    }
    return render(request, "resumen.html", contexto)
