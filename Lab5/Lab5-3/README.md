## Estudiante: Samuel Meneses Diaz, smenesesd@eafit.edu.co
## Materia: Topicos especiales de telematica
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co 
#
# Lab 5-3-Mapreduce
# 1. Breve descripción de la actividad
En este laboratorio se hizo uso y se inicio un nuevo conocimiento realizando un programa en Map/Reduce con hadoop, con ejercicios básicos.   

Libreria usada:
- MRJOB version (0.7.4); instalacion en la terminal de VSCode ```pip install mrjob```

MRJOB es una libreria de python usada para mapReduce, puede ser utilizada localmente o desde el EMR que habiamos creado en el lab 5-1 y reutilizado en el lab 5-2

Entonces para mejorar estas practicas de Map/Reduce hicimos ejercicios basicos.

## 1er punto
Se tiene un conjunto de datos, que representan el salario anual de los empleados formales en Colombia por sector económico, según la DIAN.

1.1 El salario promedio por sector economico (SE)   
Codigo: 
[Codigo1.1](https://github.com/smenesesd/TopicosTelematica/blob/main/Lab5/Lab5-3/1/PromedioSector.py)   
Resultado:
![Codigo1.1Img](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-3/img/1/promedio%20por%20sector%20Economico.png)

1.2 El salario promedio por empleado
Codigo:   
[Codigo1.2](https://github.com/smenesesd/TopicosTelematica/blob/main/Lab5/Lab5-3/1/SalarioPromedioEmpleado.py)   
Resultado:   
![Codigo1.2Img](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-3/img/1/SalarioPromedioEmpleado.png)

1.3 Numero de SE por empleado que ha tenido a lo largo de la estadistica   
Codigo:   
[Codigo1.3](https://github.com/smenesesd/TopicosTelematica/blob/main/Lab5/Lab5-3/1/estadisticaEmpleado.py)   
Resultado:   
![Codigo1.3Img](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-3/img/1/EstadisticaEmpleados.png)

## 2do punto
Se tiene un conjunto de acciones de la bolsa, en la cual se reporta a diario el valor promedio por accion, la estrucutura de los datos es (archivo: dataempresas.txt)

2.1 Por acción, dia-menor-valor, día-mayor-valor   
Codigo:   
[Codigo2.1](https://github.com/smenesesd/TopicosTelematica/blob/main/Lab5/Lab5-3/2/diaMenorValorMayorValor.py)   
Resultado:   
![Codigo2.1Img](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-3/img/2/diaMenorValorMaYORvALOR.png)

2.2 Listado de acciones que siempre han subido o se mantienen estables.
Codigo:   
[Codigo2.2](https://github.com/smenesesd/TopicosTelematica/blob/main/Lab5/Lab5-3/2/accionesSubida.py)   
Resultado:   
![Codgio2.2Img](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-3/img/2/accionesSubida.png)

2.3 DIA NEGRO: Saque el día en el que la mayor cantidad de acciones tienen el menor valor de acción (DESPLOME), suponga una inflación independiente del tiempo.
Codgio:   
[Codigo2.3](https://github.com/smenesesd/TopicosTelematica/blob/main/Lab5/Lab5-3/2/BlackDay.py)

## 3er punto
Se tiene un conjunto de datos en el cual se evalúan las peliculas con un rating

3.1 Número de películas vista por un usuario, valor promedio de calificación
Codigo:   
[Codigo3.1](https://github.com/smenesesd/TopicosTelematica/blob/main/Lab5/Lab5-3/3/peliculaVistaPorUsuario.py)   
Resultado:
![Codigo3.1Img](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-3/img/3/peliculasVistasPorUsuario.png)

3.2 Día en que más películas se han visto
Codigo:   
[Codigo3.2](https://github.com/smenesesd/TopicosTelematica/blob/main/Lab5/Lab5-3/3/diaDeMasPeliculas.py)   
Resultado:   
![Codigo3.2Img](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-3/img/3/diademasPeliculas.png)

3.3 Día en que menos películas se han visto
Codigo:   
[Codigo3.3](https://github.com/smenesesd/TopicosTelematica/blob/main/Lab5/Lab5-3/3/diaDeMenosPeliculas.py)   
Resultado:   
![Codigo3.3Img](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-3/img/3/diademenorpeliculas.png)

3.4 Número de usuarios que ven una misma película y el rating promedio
Codigo: 
[Codigo3.4](https://github.com/smenesesd/TopicosTelematica/blob/main/Lab5/Lab5-3/3/usuarioRating.py)   
Resultado:
![Codigo3.4Img](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-3/img/3/UsuarioRating.png)

3.5 Día en que peor evaluación en promedio han dado los usuarios
Codigo:   
[Codigo3.5](https://github.com/smenesesd/TopicosTelematica/blob/main/Lab5/Lab5-3/3/DiaPeorEvaluacion.py)   
Resultado:   
![Codigo3.5Img](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-3/img/3/DiaPeorEvaluacion.png)

3.6 Día en que mejor evaluación han dado los usuarios
Codigo:
[Codigo3.6](https://github.com/smenesesd/TopicosTelematica/blob/main/Lab5/Lab5-3/3/DiaMejorEvaluacion.py)   
Resultado:   
![Codigo3.6Img](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-3/img/3/diaMejorEvaluacion.png)

3.7 La mejor y peor película evaluada por genero
Codigo:   
[Codigo3.7](https://github.com/smenesesd/TopicosTelematica/blob/main/Lab5/Lab5-3/3/mejoryPeorEvaluada.py)   
Resultado:   
![Codigo3.7Img](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-3/img/3/MejoryPeorEvaluada.png)

