# Backend Assets

Backend creado con Django y Django Rest Framework para prueba técnica Assets. La base de datos utilizada es SQLite que viene por defecto con Django. 
Los commandos asumen que se esta usando un os linux o unix. En el caso de usar windows buscar comandos equivalentes.

## Instalación

1. Clona en repositorio 
```bash
   git clone git@github.com:NicolasGarcesAbarca/assets_back.git
```
2. Crea un virtual environment con python 3
```bash
   python3 -m venv env
```
3. Activa el virtual environment
```bash
   source env/bin/activate
```
4. Instala dependencias con pip usando el archivo requirements.txt
```bash
   pip install -r requirements.txt
```
5. Copia el archivo database.ini dentro de /scripts

6. Ejecuta migraciones en django
```bash
   python manage.py migrate
```
7. Muévete dentro de /scripts y ejecuta main.py para poblar la base de datos.
```bash
   cd scripts
   python main.py
```
8. Ejecuta el servidor
```bash
   python manage.py runserver
```
