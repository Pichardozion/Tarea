##Bienvenido al repositorio para ejecutar la tarea del alumno Pablo Emmanuel Pichardo Román de MTI/UPEMOR

#### Introducción

El proyecto está implementado en el framework de desarrollo web de código abierto Django, que es escrito en Python y se basa en el modelo vista-controlador.

Este proyecto final consiste en  desplegar una página web que muestra una lista de encuestas (tipos de energías renovables) con sus respectivas pregunta s y respuestas.

El sistema consiste en un formato de varias encuestas que corresponden a cada categoría; En este caso a 3 tipos de energías renovables (Fotovoltaica, Eólica y Celdas de Combustible). En cada una de ellas hay preguntas relacionadas con el su categoría y genera un proceso de votación para ir incrementando y conocer el total. 

**Instalación:**

-  Crear una carpeta en el ordenador en la ubicación en donde se desee instalar el proyecto

- Dentro de la carpeta, inicializaremos el Git Bash.

- Introducir el siguiente comando para clonar el proyecto de GitHub:

**git clone https://github.com/Pichardozion/Tarea.git**

- Se deben realizar las migraciones:

**python manage.py makemigrations
python manage.py migrate**

- Por último basta con arrancar el proyecto:

**python manage.py runserver**