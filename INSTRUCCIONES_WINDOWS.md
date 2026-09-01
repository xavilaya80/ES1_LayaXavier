# Como ejecutar ReservaGol en Windows

## 1. Abrir el proyecto

Descomprime `ES1_LayaXavier.zip`. Abre VS Code, selecciona **Archivo > Abrir carpeta** y elige la carpeta `ES1_LayaXavier`.

Abre **Terminal > Nueva terminal**. Todos los comandos siguientes se ejecutan dentro de esa carpeta.

## 2. Crear y activar el entorno virtual

En PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activacion, ejecuta una vez:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Cuando funcione, la terminal comenzara con `(.venv)`.

## 3. Instalar los paquetes

```powershell
py -m pip install -r requirements.txt
```

## 4. Crear el archivo privado `.env`

```powershell
Copy-Item .env.example .env
```

El `.env` queda solo en tu computador y `.gitignore` impide subirlo. Para esta evaluacion local, la clave de plantilla permite ejecutar Django; puedes reemplazarla por otra clave de desarrollo si deseas.

## 5. Probar el programa de consola

```powershell
py solucion.py
```

Prueba estos casos, ejecutando nuevamente el comando para cada uno:

| Caso | Hora | Jugadores | Resultado esperado |
|---|---:|---:|---|
| Aceptada | 19 | 12 | Aceptada |
| Capacidad | 20 | 18 | Rechazada por capacidad |
| Horario | 23 | 10 | Rechazada por horario |
| Invalido | -2 | 10 | Dato invalido |

Cada prueba se agrega a `datos.json` y el historial aparece con `tabulate`.

## 6. Revisar Django

No ejecutes `makemigrations` ni `migrate`, porque esta evaluacion no utiliza base de datos.

Primero comprueba la configuracion:

```powershell
py manage.py check
```

Luego inicia el servidor:

```powershell
py manage.py runserver
```

Abre en el navegador:

```text
http://127.0.0.1:8000/reservas/
```

Para detener el servidor, vuelve a la terminal y presiona `Ctrl + C`.

## 7. Entrega

Antes de subir al AAI, confirma que el ZIP se llame `ES1_LayaXavier.zip` y que no contenga `.env`, `.venv`, `db.sqlite3` ni carpetas `__pycache__`.

El archivo `ia.md` es un borrador coherente con el trabajo realizado. Leelo y ajusta cualquier frase para que refleje exactamente lo que tu hiciste y puedas explicarlo en clases.
