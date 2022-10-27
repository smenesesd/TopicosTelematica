## Estudiante: Samuel Meneses Diaz, smenesesd@eafit.edu.co
## Materia: Topicos especiales de telematica
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co 
#
# Lab 5-1-Aws-EMR
# 
# Creacion de cluster
__Primer paso para la creacion del closter:__   
   ![Ccloster1](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/Ccloster1.png)

__Segundo paso:__      
   ![version](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/version.png)   
Se escoge la version EMR en la que se va a basar el cluster

__Tercer paso:__   
   ![ComponentesSeleccionados](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/ComponentesSeleccionados.png)   
Se escogen los componentes con los que vamos a trabajar

__Cuarto paso:__      
   ![IntegracionDelCatalogoGlue](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/integracionDelCatalogoGlue.png)   
Se escogen las dos opciones que dan para hacer la integracion del catalogo Glue

__Quinto paso:__   
   ![ConfigBucket](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/configBucket.png)   
Se hace la configuracion del bucket basandonos en el documento de AWS sobre la configuracion de persistencia para Notebooks en amazon S3

__Sexto paso:__   
   ![CambiodeHW](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/cambioDeHW.png)   
Se hace el cambio de HW para el M4.xlarge, ya que el que viene por defecto no deja correrlo por ser AWS academy

__Septimo paso:__   
   ![terminygb](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/terminygb.png)   
Se configura la terminacion automatica del cluster y se aumenta la cantidad de gb

__Octavo paso:__   
   ![nombreCluster](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/nombreCluster.png)   
Se hace la eleccion del cluster name

__Noveno paso:__   
   ![claveEC2](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/claveEC2.png)   
Se hace la configuracion de la clave EC2, en este caso puse la que habia hecho para el trabajo en redis

__Decimo paso:__   
   ![awsCluster](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/AWScluster.png)   
Se verifica en la pestaña de cluster que su cluster este en proceso de creacion, esto puede llegar a durar 25 min o mas. 

__Verificacion del lanzamiento del cluster:__   
   ![clusterReady](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/clusterReady.png)   
   Se verifica la creacion exitosa de nuestro cluster

# Creacion de bucket
__Pagina Principal de S3 para la creacion de nuestro bucket:__   
   ![1](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/1.png)

__Creacion del bucket:__   
  ![2](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/2.png)   
  Se hace la creacion del bucket simplemente cambiandole el nombre como lo habiamos puesto en la persistencia para el notebook

__DNS para la conexion del master:__   
  ![3](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/4.png)   
  ![4](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/5.png)   
  - Comprobe la conexion al master desde dos maquinas diferentes, desde un S.O apple y desde un windows 
  - Nos metemos a el cluster creado y nos conectamos al master medio SSH

__Comandos para verificar el sistema de almacenamiento HDFS:__   
  ![ComandosparasistdeaAlma](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/ComandosparasistdeAlma.png) 

__Ingreso a HUE:__   
  ![configdeHUE](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/configdeHUE.png)   
  Aqui podemos ver que ya entramos al main de HUE y ya se habilitaron los puertos necesarios para la elaboracion de este lab5

__Creacion de archivos DHFS:__   
  ![archivosDHFS]()   
  En este SS, se muestra la interfaz de files (DHFS) y como se creo una carpeta llamada datasets para probar esta herramienta