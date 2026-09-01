"""Logica de negocio y programa de consola de ReservaGol."""

import json
from pathlib import Path

from tabulate import tabulate


ARCHIVO_DATOS = Path(__file__).resolve().parent / "datos.json"


def decidir_reserva(hora, jugadores):
    """Devuelve el estado y el motivo de una solicitud de reserva."""

    if hora < 0 or hora > 23 or jugadores <= 0:
        estado = "Dato invalido"
        motivo = "La hora o la cantidad de jugadores no es valida."
    elif jugadores > 14:
        estado = "Rechazada por capacidad"
        motivo = "Se supera la capacidad maxima de 14 jugadores."
    elif hora < 9 or hora > 22:
        estado = "Rechazada por horario"
        motivo = "La cancha esta fuera de su horario de funcionamiento."
    elif hora >= 9 and hora <= 22 and jugadores >= 1 and jugadores <= 14:
        estado = "Aceptada"
        motivo = "La solicitud cumple con el horario y la capacidad permitida."
    else:
        estado = "Dato invalido"
        motivo = "No fue posible procesar los datos ingresados."

    return estado, motivo


def cargar_registros():
    """Lee datos.json; si no existe o esta vacio, devuelve una lista vacia."""

    if not ARCHIVO_DATOS.exists():
        return []

    try:
        with ARCHIVO_DATOS.open("r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)
            return contenido if isinstance(contenido, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def guardar_registro(nombre, hora, jugadores):
    """Decide, guarda y devuelve una solicitud de reserva."""

    estado, motivo = decidir_reserva(hora, jugadores)
    registro = {
        "nombre": nombre.strip() or "Sin nombre",
        "hora": hora,
        "jugadores": jugadores,
        "estado": estado,
        "motivo": motivo,
    }

    registros = cargar_registros()
    registros.append(registro)

    with ARCHIVO_DATOS.open("w", encoding="utf-8") as archivo:
        json.dump(registros, archivo, ensure_ascii=False, indent=2)

    return registro


def mostrar_tabla(registros):
    """Muestra los registros con el paquete externo tabulate."""

    if not registros:
        print("Todavia no existen solicitudes guardadas.")
        return

    columnas = ["nombre", "hora", "jugadores", "estado", "motivo"]
    filas = [[registro.get(columna, "") for columna in columnas] for registro in registros]
    print(tabulate(filas, headers=["Nombre", "Hora", "Jugadores", "Estado", "Motivo"], tablefmt="grid"))


def main():
    """Solicita una reserva desde la terminal y muestra el historial."""

    print("=" * 58)
    print("RESERVAGOL - SOLICITUD DE CANCHA DE FUTBOL")
    print("=" * 58)

    nombre = input("Nombre de quien reserva: ").strip()

    try:
        hora = int(input("Hora solicitada (0 a 23): "))
        jugadores = int(input("Cantidad de jugadores: "))
    except ValueError:
        print("\nDato invalido: la hora y los jugadores deben ser numeros enteros.")
        return

    registro = guardar_registro(nombre, hora, jugadores)

    print("\nResultado de la solicitud")
    print(f"Estado: {registro['estado']}")
    print(f"Motivo: {registro['motivo']}")
    print("\nHistorial guardado en datos.json")
    mostrar_tabla(cargar_registros())


if __name__ == "__main__":
    main()
