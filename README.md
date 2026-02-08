Descripción:
Con este repositorio vamos a hacer un proxy inverso usando Docker. Se necesita una API en Flask, una base de datos en Redis y un proxy inverso utilizando Nginx.

Diagrama:
![diagrama](croquis.png)

Instrucciones de Despliegue:
git clone https://github.com/dgaldel1008/practica_seguridad.git
cd practica_seguridad
docker-compose up --build

Pruebas:
curl -i http://localhost

curl -i http://localhost
