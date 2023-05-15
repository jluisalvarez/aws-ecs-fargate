# Docker, python y Flask (Hola Mundo)


## Crea la aplicación

Crea un entorno virtual, actívalo e instala Flask.
(aquí no crearemos el entorno vírtual, pero es muy aconsejable hacerlo)

```shell
$ pip3 install flask
```

Implementa la aplicación, por ejemplo en el fichero app.py:

```python
# file app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def holamundo():
    return 'Hola Mundo!'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            debug=True,
            port=8080)


```

Prueba la aplicación en local


```shell
$ python3 app.py
```



## Contruir la imagen

Crea el fichero Dockerfile

```
FROM python:3.6

WORKDIR /app

COPY ./app /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]

```

Construye la imagem

```shell
$ docker build --tag jluisalvarez/hm-python:2023 .
```

Prueba la imagen en local

```shell
$ docker run -d --name hmpython -p 8080:8080 jluisalvarez/hm-python:2023
```

Sube la imagen a Docker Hub

```shell
$ docker login

...

$ docker push jluisalvarez/hm-python:2023

```

# Despliaga en AWS ECS - Fargate

## Crea un cluster

Un clúster en ECS es un concepto lógico que permite la agrupación de contenedores
que se ejecutarán en máquinas virtuales específicas (EC2) o en infraestructura Serveless (Fargate). Para crearlo:

En la consola Web AWS, accede a Amazon Elastic Container Service.

Selecciona la opción "Clusters" y clic en "Crear Cluster"

Introduce un nombre para el clúster, por ejemplo: clusterECSFargate

En Redes, elige la VPC y las subredes donde se desplegará (aquí usaremos las opciones por defecto, todas las subredes de la VPC por defecto)

En Infraestructura, selecciona la opción AWS Fargate (que estará seleccionada por defecto)

En Monitoreo y Etiquetas, también lo dejaremos por defecto.


## Crea una definición de tarea

En la consola Web AWS, en Amazon Elastic Container Service.

Selecciona la opción "Definiciones de Tareas" y clic en "Crear una nueva definición de Tarea"

En el primer paso, establecemos un nombre, por ejemplo, hm-python y en contenedor 1, estableceremos un nombre para el contenedor, 
por ejemplo hmpython, y la imagen para el contenedor (registry.hub.docker.com/jluisalvarez/hm-python:2023). El resto de opciones la dejamos por defecto.

En el segundo paso, establecemos la configuración del entorno, AWS Fargate, Linux, 0.5 CPU, Memoria 1Gb y en rol de tarea y de ejecución, seleccionamos LabRole, 
dejando el resto de opciones por defecto.

En el tercer paso, revisamos y le damos a "Crear".

## Ejecutar una tarea o un servicio

Una tarea es un con

En la consola Web AWS, accede a Amazon Elastic Container Service, opción "Clusters" y accedemos a nuestro cluster (clusterECSFargate)

Accedemos a la pestaña Tareas y creamos una nueva tarea. 

En Configuración Informática, seleccionamos Tipo de lanzamiento. 

En Configuración de implementación, seleccionamos Tarea.

En Familia, seleccionamos la definición de tarea a ejecutar y la versión deseada.

En Redes, seleccionamos la VPC y el grupo de seguridad, activando la opción de IP pública.

El resto de opciones pueden dejarse por defecto.














