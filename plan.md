# Plan del proyecto: ReservaGol

## 1. Apartado de negocio

### Problema

En muchos complejos deportivos las solicitudes de reserva de canchas se reciben por mensajes o llamadas. La persona encargada debe revisar manualmente si el horario solicitado esta dentro del horario de funcionamiento y si la cantidad de jugadores no supera la capacidad. Esto consume tiempo y puede producir reservas imposibles o mal registradas.

### Solucion

ReservaGol recibe los datos de una solicitud y determina automaticamente si puede aceptarse. El programa informa el motivo exacto, guarda el resultado en un archivo JSON y permite consultar el historial en consola y en una pagina Django.

### Alcance

Esta version permite ingresar el nombre, la hora y la cantidad de jugadores; validar una solicitud; entregar uno de cuatro resultados; guardar cada registro en `datos.json`; mostrar una tabla en consola y mostrar/crear reservas desde una sola pantalla web.

No incluye base de datos, cuentas de usuario, inicio de sesion, pagos, mapas, API, aplicacion movil, multiples complejos ni torneos.

### Priorizacion MoSCoW

**Must (MVP que se programa)**

1. Pedir nombre, hora y cantidad de jugadores.
2. Validar la solicitud y entregar uno de cuatro resultados con su motivo.
3. Guardar las solicitudes en `datos.json`.
4. Mostrar el historial con `tabulate` en consola.
5. Reutilizar la logica en una sola pantalla Django.

**Should (no se programa en esta version)**

- Corregir o eliminar una solicitud anterior.
- Seleccionar distintos tipos de cancha.
- Mostrar estadisticas de aceptacion y rechazo.

**Could (posible version futura)**

- Calendario visual de disponibilidad.
- Calculo automatico del precio.
- Busqueda por fecha o nombre.

**Won't (fuera de esta version)**

- Base de datos SQL, login, pagos, API, mapas y aplicacion movil.

## 2. Apartado tecnico

### Datos de entrada

| Dato | Tipo | Uso |
|---|---|---|
| `nombre` | `str` | Identifica a quien solicita la reserva. |
| `hora` | `int` | Hora solicitada entre 0 y 23. |
| `jugadores` | `int` | Cantidad de personas que usaran la cancha. |

### Regla de decision

La cancha funciona desde las 09:00 hasta las 22:00 y acepta como maximo 14 jugadores. Las condiciones se revisan en este orden:

1. **Dato invalido:** `hora < 0`, `hora > 23` o `jugadores <= 0`.
2. **Rechazada por capacidad:** `jugadores > 14`.
3. **Rechazada por horario:** `hora < 9` o `hora > 22`.
4. **Aceptada:** hora entre 9 y 22 y jugadores entre 1 y 14.

Cada resultado tiene un mensaje diferente que explica el motivo.

### Paquete externo

Se utiliza `tabulate` para presentar los registros de `datos.json` como una tabla ordenada en la consola. Tambien se usan Django para la pantalla web y python-decouple para leer las variables de `.env`.

### Almacenamiento

Cada solicitud se guarda como un objeto dentro de la lista de `datos.json`, con nombre, hora, jugadores, estado y motivo. No se utiliza una base de datos.

### Pantalla web

La direccion principal es `/reservas/`. Una sola vista muestra un formulario, el resultado de la solicitud y el historial. La vista importa desde `solucion.py` la funcion que decide y guarda, por lo que la regla no se escribe dos veces.
