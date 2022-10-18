# info de la materia: Tópicos especiales de telematica 
# Estudiante: Samuel Meneses Diaz, smenesesd@eafit.edu.co
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
# Laboratorio04 Aplicacion monolitica con balanceo y datos distribuidos (BD y archivos)
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

   ![ssl2](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/ssl2.png)
# 2. Informaión general de diseño de alto nivel, arquitectura, patrones , mejores practicas utilizadas.
- Se hizo uso de docker compose para definir y ejecutar aplicaciones de Docker de varios contenedores.
__ComposerVersion:__

  ![ComposeV](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/composeVersion.png)
- Se hizo uso de un archivo YAML del docker compose para configurar los servicios de las aplicaciones.   
__YAMLwp1:__

   ![YAMLwp1](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/YAMLwp1.png)

- Se hizo uso de contenedores para aislar los dos wordpress, loadBalancer y el dbServer.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programacion, librerias, paquetes, etc, con sus numeros de versiones.
- Se hizo uso de docker compose version ``` 3.7 ```

__ComposerVersion:__

  ![ComposeV](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/composeVersion.png)

- Nginx como servidor web en su version ```1.18.0```
- MySQl como dbServer en su version ```8.0.29```
- GCP suite de aplicaciones en nube 
- S.O ```Ubuntu 20.04```

## Wordpress
- Para ingresar a la maquina de wordpress1:
```IP: 34.122.154.199```

  __ConexionaWP1:__

  ![ConexionaWP1](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/conexionawp1.png)

- Para ingresar a la maquina de wordpress2:
```IP: 35.226.63.203```

  __ConexionaWP2:__

  ![ConexionaWP2](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/conexionawp2.png)

- Se hizo la instalacion de nginx en los dos wordpress

  __InstalacionNginxWP:__

  ``` sudo apt install nginx -y```
  ![nginxwp](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/nginxwp.png)

- Instalacion de docker y docker compose:

  __Instalacion Docker:__

  ![InstalacionDocker](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/instalacionDocker.png)
 
- Execute docker compose:

  ```sudo docker-compose up --build -d```
- Se hizo la instalacion de common que sera la carpteta compartida en el nfs, el cual es instalado con el comando ``` sudo apt install nfs-common``` en los dos wordpress

  __Instalacion Common:__
  ![InstalacionCommon](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/instalacionCommon.png)
   - Se debe de configurar el archivo ubicado en ```/etc/fstab``` de cada wordpress para los archivos compartidos

     __Fstab:__

     ![Fstab](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/fstab.png)
 - Verificacion de la pag web tenga su certificado SSL y entre al wp admin desde el DNS   

   __wp-admin:__
  ![wpadmin](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/wpadmin.png)

## Loadbalancer
- Para ingresar al loadbalancer:

  ``` IP:34.173.65.3```

  __Conexion a LB:__

  ![ConexionLB](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/conexionLoadB.png)

- Instalacion de docker y docker compose:

  __Instalacion Docker:__

  ![InstalacionDocker](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/instalacionDocker.png)

- Instalacion de nginx:

  ``` sudo apt install nginx -y```

- Se realizo un clonacion del github del profe en la carpeta ```st0263-2022-2``` 
- Se modifica el archivo ```etc/nginx/nginx.conf```

  __nginxconf:__

  ![nginxconf](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/nginxconf.png)

- Se modifica el docker-compose ```docker-compose.yml```

  __docker-composeLB:__

  ![docker-composeLB](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/docker-composeLB.png)

- Se instalo letsencrypt y certbot

  __ssl:__
   
   ![ssl](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/ssl.png)   
  __ssl2:__

   ![ssl2](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/ssl2.png)

- Execute docker-compose

  __ExecuteDC:__

  ![esecuteDC](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/executeDC.png)

- SSl conf

  __ssl conf:__

  ![ssl conf](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/sslconfig.png)

- Configuracion de nginx con ssl

  __sslNginxConf:__

  ![sslNginxConf](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/sslnginxconf.png)

## DBServer
- Para ingresar a la base de datos:

   ```IP: 34.171.143.167```

   __dbServerconexion:__
   ![dbserverconection](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/dbservercon.png)

- Intalacion de docker:

  __Install docker:__
  ![InstalldockerDB](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/dockerdb.png)

- Configuracion del archivo ```docker-compose.yaml```

  __dbdockerCompose:__
  ![dbDC.yaml](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/dbDCYAML.png)

- ``` sudo docker-compose up -d```

  __up:__

  ![DCUp](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/DCup.png)

- Conexion a mySQL:

  __Conexion a MYSQL:__

  ![mySQL](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/mySQLDB.png)

- Configuracion de mySQL:

  __config mySQL:__

  ![configmySQL](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/configmysql.png)
  ![configmy](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/configmy.png)

## NFS
- Se hace la descarga de nfs kernel ```sudo apt install nfs-kernel-server```

  __Instalacion nfs kernel server:__
  ![nfskernelserver](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/nfsserverkernel.png)

- Se crea la carpeta share

  __Creacion de carpeta share:__
  ![CarpetaShare](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/master/lab04/img/CarpetaShare.png)

- Configuracion de acceso a los archivos compartidos:

  __etc/exports:__
  ![archCompartidos]()

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programacion, librerias, paquetes, etc, con sus numeros de versiones.


# 5. Evidencia