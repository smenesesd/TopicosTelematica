# info de la materia: Tópicos especiales de telematica 
# Estudiante: Samuel Meneses Diaz, smenesesd@eafit.edu.co
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
# <Laboratorio04 Aplicacion monolitica con balanceo y datos distribuidos (BD y archivos)>
# 1. Breve descripcion de la actividad
Se hizo un laboratorio basado en el lab03 en la cual se habia desplegado una aplicacion monolitica basada en contenedores en un solo servidor con un dominio ```smenesesd.tk ``` y un certificado SSL, la mejora que se le hizo a este laboratorio basado en lo anteriormente dicho fue mejorar la disponibilidad siendo dividida en varios nodos.

## 1.1 Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor. (Requerimientos funcionales y no funcionales)
-  Se desplegaron dos maquinas virtuales de wordpress en GCP, cada una con su direccion IP elastica  
__wpress1:__
![wpress1](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/wp1.png)
__wpress2:__
![wpress2](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/wp2.png)
- Se desplego una VM para la creacion de el balanceador de carga usando NGINX, el cual se encarga de redireccionar al wp1 o wp 2 dependiendo de la entrada de trafico al LB, de tal manera se uso nginx para el dominio y el certificado como el lab03  
__loadbalancer:__
![loadbalancerIP](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/lbalancerIP.png)
- Se desplego una VM en la cual estara ubicada el DataBase Server   
__dbServer:__
![dbserverIP](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/dbserver.png)
- Se desplego un VM llamada nfs, el cual es un servidor en el cual estaran los archivos compartidos de los dos wordpress   
__nfs:__
![nfs](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/nfs.png)
- Se habilito el puerto 443 para HTTPS protocol. 
- Se creo un Cloud DNS el cual GCP da la facilidad de enlazarlo con tu DNS que en mi caso seria ``` smenesesd.tk ```. En los detalles de zona se agregaron conjuntos de registros de tipo TXT, CNAME, A, NS, SOA.   
__cloudDNS:__
![cloudDNS](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/cloudDNS.png)
- Como el lab03 se utilizo certbot y letsencrypt para generar y tener la gestion del certificado ssl y el cifrado HTTPS de los wordpress.   
__ssl:__
![ssl](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/ssl.png)   
__ssl2:__
![ssl2]()
# 2. Informaión general de diseño de alto nivel, arquitectura, patrones , mejores practicas utilizadas.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programacion, librerias, paquetes, etc, con sus numeros de versiones.

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programacion, librerias, paquetes, etc, con sus numeros de versiones.

# 5. Evidencia