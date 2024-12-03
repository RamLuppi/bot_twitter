Este repositorio contiene un script en Python que combina la funcionalidad de la API de fútbol de RapidAPI con la API de Twitter para publicar automáticamente información sobre los partidos de fútbol de dos equipos específicos en Twitter. El script está configurado para manejar zonas horarias y se centra en los equipos Estudiantes de La Plata y Gimnasia y Esgrima La Plata.

*Funcionalidades principales*
  -Consulta de datos de partidos:
    Utiliza la API de fútbol (RapidAPI) para obtener información detallada sobre los próximos partidos de un equipo, filtrados por fecha y       temporada.
  -Publicación en Twitter:
    Publica un tweet automático con los detalles del partido del día (si existe) usando la API de Twitter.
  -Soporte para múltiples equipos:
    Actualmente, está configurado para dos equipos (Estudiantes y Gimnasia), pero es fácil de expandir para otros equipos agregando sus IDs      en el diccionario.
  -Manejo de zona horaria:
    Ajusta las fechas y horas a la zona horaria de Buenos Aires (Argentina).
  -Mensajes personalizados:
    Los tweets incluyen detalles como los equipos que juegan, la sede del partido y la fecha.
  
Cuenta de twitter con el codigo aplicado: @PinchaTriperoLP
