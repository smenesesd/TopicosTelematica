# info de la materia: Tópicos especiales de telematica 
#
# Estudiante: Samuel Meneses Diaz, smenesesd@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
# <Laboratorio03 Docker - wordpress>
#
# 1. breve descripción de la actividad
#
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
 - Se creo una instancia en google cloud con un sistema operativo linux/Ubuntu
 - Se hizo uso de la aplicacion PuTTy key generator, para la creacion de dichas claves ssh privada y otra clave ssh publica
 - Creacion de una IP elastica para que no hayan cambios en la IP externa de la instancia de GCP
 - Se dieron los permisos del domino en cloud DNS
 - Permisos tipo A, CNAME, NS, SOA y TXT 
 - Se instalo docker, y se configuro para ejecutar la app de manera aislada pero en el mismo servidor 
 - Se hizo uso de una autoridad de certificacion llamada let's encrypt y certbot
 - Se configuro el let's encrypt para un servidor https y que este genere un certificado valido para la pagina web wordpress
 - se instalo y se configuro un servidor web llamado NGINX que es open source para el contenido estatico del sitio web
 - Se instalo y se configuro wordpress

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

 - Se implemento todo lo solicitado por el profesor Edwin. 

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
 La propuesta de solucion para este laboratorio es desarrollar habilidades en los procesos de creacion, despliegue y gestion de aplicaciones utilizando contenedores, en este caso especifico, usando Docker. La teconologia usada fue wordpress que es un sistema de gestion de contenidos web.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

 No se hizo uso de un lenguaje de programacion en especifico, se hizo uso de la terminal de Ubuntu para la solucion de este proyecto. Se hizo uso de Ubuntu en la version(20.04), nginx en la version(1.18.0) y Certbot en la version(1.22).
 `IP Externa: 35.225.119.105 `
 `Dominio: smenesesd.tk`
 `URL: https://www.smenesesd.tk/ `

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
 Para la solucion de este proyecto se uso Ubuntu, docker ,nginx, letsencrypt, certbot y wordpress para la creacion y despliegue de la aplicacion para ser aplicada usando contenedores.
 `IP Externa: 35.225.119.105 `
 `Dominio: smenesesd.tk`
 `URL: https://www.smenesesd.tk/ `

 Si desea visitar la pagina web(wordpress), lo invito a ir a su buscador de preferencia y poner en la barra de busqueda el siguiente URL: `https://www.smenesesd.tk/ `, ahí encontrara el wordpress con sus respectivos permisos, siendo esta una pagina segura de navegar y viendo la solucion implementada en base al problema del lab03.


# 5. Evidencia
---
__Info basica de instancia:__
![1](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/1.png)

---

__Creacion de PuTTy key:__
![2](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/2.png)

---

__Clave Cliente SSH:__
![3](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/3.png)

---

__Conexion en la consola:__
![4](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/4.png)

---

__IP estatica:__
![5](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/5.png)

---

__Dominios freenom:__
![6](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/6.png)

---

__Remove docker:__
![8](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/8.png)

---

__Update e instalacion de docker:__
![9](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/9.png)

---

__Compose docker:__
![10](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/10.png)

---

__Install git:__
![11](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/11.png)

---

__Enable docker:__
![12](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/12.png)

---

__Usermod:__
![13](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/13.png)

---

__Install letsencrypt:__
![14](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/14.png)

---

__Install nginx:__
![15](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/15.png)

---

__Nginx config:__
![16](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/16.png)

---

__nameservers:__
![18](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/18.png)

---

__nginx -t:__
![19](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/19.png)

---

__evidencia de conection nginx:__
![20](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/20.png)

---

__letsencrypt:__
![21](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/21.png)

---

__certbot:__
![22](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/22.png)

---

__Creacion de carpetas wordpress y ssl:__
![23](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/23.png)

---

__Openssl dhparam:__
![24](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/24.png)

---

__Safe:__
![25](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/25.png)

---

__Git clone:__
![26](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/26.png)

---

__Stop nginx:__
![27](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/27.png)

---

__docker build:__
![28](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/28.png)

---

__start docker:__
![29](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/29.png)

---

__Primer intento Fallido:__
![30](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/30.png)

---

__Segundo intento ya seguro:__
![31](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/31.png)

---

__Admin de wp:__
![32](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/32.png)

---

__Conexion segura:__
![33](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/33.png)

---

__Certificado valido:__
![34](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/34.png)

---

__wp con https:__
![35](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/Laboratorio3/img/35.png)

---



# referencias:

## https://github.com/st0263eafit/st0263-2022-2/blob/main/docker-nginx-wordpress-ssl-letsencrypt/README.md
## https://interactivavirtual.eafit.edu.co/d2l/le/content/103481/viewContent/492273/View
## https://console.cloud.google.com/compute/instances?project=topicostelematica-362318
## https://my.freenom.com/clientarea.php?action=domains

#### versión README.md -> 1.0 (2022-Sept)