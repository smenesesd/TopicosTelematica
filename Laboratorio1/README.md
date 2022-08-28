### ST0263 Tópicos especiales en telemática
##### Estudiante: Samuel Meneses Diaz, smenesesd@eafit.edu.co
##### Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

#### 1. Breve descripcion de la actividad
##### 1.1 Requerimientos funcionales y no funcionales
- Implementar un mini-servidor Web (HTTP) minimalista sobre sockets TCP
 - Se utilizo el lenguaje de programacion Python
 - Como es un servidor Web concurrente (HTTP) va a recibir las peticiones mediante los sockets TCP y puede recibir varias conexiones a la vez.
 - Se utilizo para recibir las peticiones el purto 80 por defecto
 - Se procesa el HTTP request
 - Si se necesita algun recurso, lo busca y si no esta responde un mensaje de error. 
 -  Para responder ya sea el recurso o el mensaje de error, se responde mediante un HTTP response. 
 
##### 1.2 Aspectos no cumplidos
Todos los aspectos fueron cumplidos y el servidor trabaja como se suponia 

####2. Informacion general de diseño de alto nivel, arquitectura, patrones, mejores practicas utilizadas. 
Lo que se hizo en este laboratorio fue un servidor minimalista que solo sea capaz de interpretar el metodo GET y devolver lo que se solicito, si lo tiene lo devuelve y si no te devuelve un mensaje de error, esto fue  basado en el protocolo HTTP 0.9, implementando una arquitectura de capas.

####3. Descripcion del ambiente de desarrollo y técnico
Este laboratorio fue hecho con unos pedazos de codigo de un proyecto de la materia de telematica TelematicaProyecto2,El proyecto anteriormente mencionado fue hecho con un compañero de grupo llamado David Gomez Correa. La diferencia con el proyecto de Telematica fue que se eliminaron varias partes ya que solo estare utilizando el request GET, utilizando el protocolo HTTP v0.9. Para la elaboracion de este mini servidor, fue utilizado el lenguaje de programacion python
Para la ejecucion es necesario tener el lenguaje de programacion python instalado en su maquina y un editor de codigo fuente de su agrado. Se necesita abrir la terminar y correr el server.py con la siguiente instruccion: python Server.py.
Librerias:
Threading: Para el control de flujo y que sea concurrente
Sockets: Para el enlace de comunicacion de dos entidades. 
Clases:
 - En la clase server es donde pasa todo lo principal como creacion del socket y la configuracion para que funcione en el protocolo TCP, tambien se abre el socket y espera conexion.
 - En la clase GET es donde pasa todo el tipo de solicitudes
 - En la clase constants es donde van a estar todas las constantes usadas en el codigo, como puerto, ip del servidor y los dichos errores con sus mensajes.

####4. Descripcion del ambiente de desarrollo y técnico (en producción)
IP: 44.196.79.246
Para la conexion al servidor lo que debe de hacer es ejecutar en la terminal server.py despues de que lo haya ejecutado ingresara a la ip dada y se encontrara en .html del codigo y ya podra ir a los diferentes recursos disponibles.

####5. Informacion importante
Este proyecto fue hecho con unos pedazos de codigo de un proyecto de la materia de telematica TelematicaProyecto2,El proyecto anteriormente mencionado fue hecho con un compañero de grupo llamado David Gomez Correa. La diferencia con el proyecto de Telematica fue que se eliminaron varias partes ya que solo estare utilizando el request GET, utilizando el protocolo HTTP v0.9.

Referencias: 
1. Respositorio del proyecto de telematica:
[Proyecto telematica](https://github.com/smenesesd/TelematicaProyecto2 "Proyecto telematica")
2. Un Protocolo estándar de comunicación entre un browser y un servidor web: HTTP:
[https://es.wikipedia.org/wiki/Protocolo_de_transferencia_de_hipertexto](https://es.wikipedia.org/wiki/Protocolo_de_transferencia_de_hipertexto)
3. Un formato de datos principal de intercambio: HTML:
[https://es.wikipedia.org/wiki/HTML](https://es.wikipedia.org/wiki/HTML)
4. Un localizador de recursos web en Internet: URL:
[https://es.wikipedia.org/wiki/Localizador_de_recursos_uniforme](https://es.wikipedia.org/wiki/Localizador_de_recursos_uniforme)








