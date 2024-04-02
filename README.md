## Requerimientos
Se debe tener instalado python 3.11

## Para iniciar aplicación

0-Configurar la base de datos

ir al archivo database_manager.py y modificar la linea 5 en la parte que dice "{aqui_tu_usuario}"
con su usuario, esto es para que no se topen y usen bases de datos distintas

los usuarios son:
* pastita
* saniel

1- Iniciar entorno virtual
Ejecutar en consola:
```
pipenv shell
```

2- Instalar Librerias
Ejecutar en consola:
```
pipenv install
```

3- Iniciar servidor
Ejecutar en consola:
```
uvicorn main:app --reload
```

Para comprobar abrir en el navegador http://127.0.0.1:8000/docs, la url de la api sera http://127.0.0.1:8000

## Posibles Problemas
En caso de que aparezca un mensaje de que no se reconoce el comando

### linux:
se puede usar pyenv

Instalar python desde pyenv
Ejecutar
```
pyenv install 3.11
```

Usar la versión 3.11
Ejecutar
```
pyenv global 3.11
```
### Windows:
En windows se puede descargar e instalar desde: https://www.python.org/downloads/release/python-3110/