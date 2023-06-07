import requests
import json
import openpyxl

# Función para obtener el precio en una región específica
def obtener_precio(appid, cc):
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}&cc={cc}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and str(appid) in data:
        game_data = data[str(appid)]
        if game_data["success"]:
            game_info = game_data["data"]
            if "price_overview" in game_info:
                price_info = game_info["price_overview"]
                return price_info.get("final_formatted", "Sin precio")
    return "Sin precio"

# Leer la lista de ID de juego desde un archivo de texto
with open("juegos.txt", "r") as file:
    juegos_ids = file.read().splitlines()

# Crear un archivo Excel y una hoja de cálculo
wb = openpyxl.Workbook()
sheet = wb.active

# Agregar encabezados de columna
sheet.append(["ID", "Nombre", "Precio Chile", "Precio Argentina"])

# Obtener la información de cada juego y agregarla al archivo Excel
for appid in juegos_ids:
    # Obtener información del juego para Argentina y Chile
    nombre_juego = ""
    precio_argentina = obtener_precio(appid, "ar")
    precio_chile = obtener_precio(appid, "cl")
    
    # Obtener el nombre del juego
    url_name = f"https://store.steampowered.com/api/appdetails?appids={appid}"
    response_name = requests.get(url_name)
    data_name = response_name.json()
    if response_name.status_code == 200 and str(appid) in data_name:
        game_data_name = data_name[str(appid)]
        if game_data_name["success"]:
            game_info_name = game_data_name["data"]
            nombre_juego = game_info_name.get("name", "Sin nombre")

    # Agregar los datos a la hoja de cálculo
    sheet.append([appid, nombre_juego, precio_chile, precio_argentina])

# Guardar el archivo Excel
wb.save("juegos_precios.xlsx")

print("La información se ha guardado en el archivo 'juegos_precios.xlsx'.")
