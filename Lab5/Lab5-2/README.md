## Estudiante: Samuel Meneses Diaz, smenesesd@eafit.edu.co
## Materia: Topicos especiales de telematica
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co 
#
# Lab 5-2-HDFS
# 1. Breve descripción de la actividad
En este laboratorio se afianzaron y se pusieron a prueba  los conocimientos en la gestion de archivos en HDFS y S3 para big data. 

__Conexion al cluster:__
![1](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/1.png)   
Nos conectamos al cluster para empezar con este lab 5-2

__listar archivos:__
![2](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/2.png)   
HDFS dfs es solo para hacer la lista de archivos HDFS

__Creacion de datasets:__
![3](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/3%20creacion_datasets.png)   
Se hace la creacion de la carpeta de datasets dentro del user hadoop

__Copia archivos locales hacia HDFS:__
![4](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/4.png)   
Se hace la copia de los archivos compilados por medio de SSH/SCP al servidor gateway por la VPN 

``` hdfs dfs -put /datasets/gutenberg/gutenberg-small.zip /user//datasets/ ```

__Verificacion de la copia de los archivos locales en el hadoop:__
![5](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/5.png)
