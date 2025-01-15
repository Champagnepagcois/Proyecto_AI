
# Manual para correr programa

Requisitos previos
Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas:

 - [Node js version =<15.14](https://nodejs.org/en/download)
 - [Python version =<3.9](https://www.python.org/downloads/)
 - [PostgreSQL version =<14](https://www.postgresql.org/download/)


Una vez descargardas asegurate de que se hayan declarado las variables de entorno con los siguientes comandos:

```bash
  node --version
```
```bash
  python --version
```
```bash
  pip --version
```
```bash
  psql --version
```
Al ejecutarlos, la consola te indicara la version de cada uno.
 
## Instalaciòn de dependencias para el frontend

Empezamos instalando las dependencias para el frontend,asi que nos ubicamos en el directorio frontend,  con el siguiente comando se muestra como:

```bash
  cd frontend
  npm install 
```


## Instalaciòn de dependencias para el backend

Empezamos instalando las dependencias para el backend,asi que nos ubicamos en el directorio backend,  con el siguiente comando se muestra como:

```bash
  cd backend
  pip install -r requirements.txt
```

## Cargamos datos a la base de datos

Empezamos iniciando la consola de postgres, hay dos maneras o en cdm escribir el comando:

```bash
psql
```
o en windos escribir la palabra sql shell (psql) e ingresamos nuestras credenciales
 y otra forma es ingresando el comando siguiente:

```bash
psql -U postgres
```

Ya que hemos ingresado colocamos el comando:
```bash
  CREATE DATABASE ecommerce;
```
una vez que hemos creado la base de datos,tnemos que ubicar la ruta de nuestro archivo de respaldo, y copiamos la ruta absoluta del archivo.
En una terminal escribiremos el sigiuente comando, agregando al final la ruta al archivo de respaldo
```bash
psql -U postgres -d ecommerce -f C://ruta_del_archivo
```




 
 
## Ejecucion localmente

Clona el proyecto

```bash
  git clone https://github.com/Champagnepagcois/Proyecto_AI.git
```

### Frontend


Ingresa al directorio frontend 

```bash
  cd frontend
```

Instala las dependencias

```bash
  npm install
```

Inicia el servidor

```bash
  npm run dev
```

### Backend

Ingresa al directorio backend 

```bash
  cd backend
```

Instala las dependencias

```bash
  pip install -r requirements.txt
```

Inicia el servidor

```bash
  python main.py
```
