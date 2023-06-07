# WenapotoStore

Este script de Python recopila información sobre los precios de juegos de Steam en Argentina y Chile y la guarda en un archivo Excel.

## Requisitos

- Python 3 instalado en tu sistema.
- Paquetes de Python requeridos: requests, json y openpyxl. Puedes instalarlos usando el administrador de paquetes pip.

## Instalación

1. Clona o descarga este repositorio en tu máquina local.
2. Abre una terminal o línea de comandos.
3. Navega hasta el directorio donde se encuentra el script Precios.py.
4. Opcionalmente, crea y activa un entorno virtual para el proyecto (recomendado).
5. Instala las dependencias ejecutando el siguiente comando:

```
pip install requests openpyxl
```

## Uso

1. Crea un archivo de texto llamado juegos.txt en el mismo directorio que Precios.py.
2. En el archivo juegos.txt, coloca los ID de juego de Steam, uno por línea.
3. Ejecuta el script Precios.py con el siguiente comando:

```
python Precios.py
```

4. El script recopilará la información de precios de los juegos especificados y creará un archivo Excel llamado juegos_precios.xlsx en el mismo directorio.

## Notas

- Asegúrate de tener una conexión a Internet activa durante la ejecución del script, ya que consulta la API de Steam para obtener la información de precios.
- Los precios en Argentina y Chile se obtienen utilizando los códigos de país ar y cl, respectivamente. Puedes modificar estos códigos en el script si deseas obtener precios de otras regiones.
