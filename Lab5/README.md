## Estudiante: Samuel Meneses Diaz, smenesesd@eafit.edu.co
## Materia: Topicos especiales de telematica
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co 
#
# Lab 5-1-Aws-EMR
# 
# Creacion de cluster
__Primer paso para la creacion del closter:__   
   ![Ccloster1](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/Ccloster1.png)

__Segundo paso:__      
   ![version](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/version.png)   
Se escoge la version EMR en la que se va a basar el cluster

__Tercer paso:__   
   ![ComponentesSeleccionados](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/ComponentesSeleccionados.png)   
Se escogen los componentes con los que vamos a trabajar

__Cuarto paso:__      
   ![IntegracionDelCatalogoGlue](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/integracionDelCatalogoGlue.png)   
Se escogen las dos opciones que dan para hacer la integracion del catalogo Glue

__Quinto paso:__   
   ![ConfigBucket](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/configBucket.png)   
Se hace la configuracion del bucket basandonos en el documento de AWS sobre la configuracion de persistencia para Notebooks en amazon S3

__Sexto paso:__   
   ![CambiodeHW](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/cambioDeHW.png)   
Se hace el cambio de HW para el M4.xlarge, ya que el que viene por defecto no deja correrlo por ser AWS academy

__Septimo paso:__   
   ![terminygb](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/terminygb.png)   
Se configura la terminacion automatica del cluster y se aumenta la cantidad de gb

__Octavo paso:__   
   ![nombreCluster](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/nombreCluster.png)   
Se hace la eleccion del cluster name

__Noveno paso:__   
   ![claveEC2](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/claveEC2.png)   
Se hace la configuracion de la clave EC2, en este caso puse la que habia hecho para el trabajo en redis

__Decimo paso:__   
   ![awsCluster](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Cluster/AWScluster.png)   
Se verifica en la pestaña de cluster que su cluster este en proceso de creacion, esto puede llegar a durar 25 min o mas. 

__Verificacion del lanzamiento del cluster:__   
   ![clusterReady](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/clusterReady.png)   
   Se verifica la creacion exitosa de nuestro cluster

# Creacion de bucket
__Pagina Principal de S3 para la creacion de nuestro bucket:__   
   ![1](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/1.png)

__Creacion del bucket:__   
  ![2](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/img/Bucket/2.png)   
  Se hace la creacion del bucket simplemente cambiandole el nombre como lo habiamos puesto en la persistencia para el notebook

__DNS para la conexion del master:__   
  ![3]()   
  ![4]()   
  Nos metemos a el cluster creado y nos conectamos al master medio SSH

