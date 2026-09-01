# Uso de inteligencia artificial

Utilice ChatGPT para ordenar la idea de ReservaGol, revisar que el problema tuviera los cuatro resultados exigidos y entender como conectar la logica de Python con una vista de Django.

Una consulta concreta fue: "Quiero crear una aplicacion de reserva de canchas de futbol. ¿Como puedo adaptarla a variables, if/elif, JSON y una sola vista Django, sin base de datos?". La respuesta propuso validar la hora y la cantidad de jugadores, guardar cada solicitud en JSON y reutilizar la misma funcion desde Django.

Al principio aparecieron funciones demasiado grandes para esta evaluacion, como pagos, usuarios, varias canchas, calendario y torneos. Las quite del MVP y las deje en las categorias Should, Could o Won't del plan. Tambien ordene las condiciones para comprobar primero el dato invalido y separe los dos rechazos: uno por capacidad y otro por horario. Revise el codigo y probe personalmente los cuatro resultados antes de preparar la entrega.
