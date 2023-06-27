import requests
import json
import openpyxl
import pandas as pd

def obtener_precio(appids,nombres):
    url = f"https://store.steampowered.com/api/appdetails?appids={','.join(appids)}&filters=price_overview&cc=ar"
    response = requests.get(url)
    data = response.json()
    results = {}
    
    if response.status_code == 200:
        count=0
        for appid in appids:
            nombre = nombres[count]
            count+=1
            if str(appid) in data:
                game_data = data[str(appid)]
                if game_data["success"]:
                    game_info = game_data["data"]
                    if "price_overview" in game_info:
                        price_info = game_info["price_overview"]
                        price_ars = price_info.get("final", "Sin precio")/100
                        price_clp = convertir_a_clp(price_ars)
                        discount_percent = price_info.get("discount_percent", "Sin precio")
                        
                        results[appid] = {
                            "ID": appid,
                            "Nombre": nombre,
                            "Precio Argentino": "ARG$ "+str(price_ars),
                            "Precio Argentino (CLP)": "CLP$ "+price_clp,
                            "Descuento": discount_percent
                        }
    
    return results


# Obtener el tipo de cambio ARS/CLP
url_tipo_cambio = "https://api.exchangerate-api.com/v4/latest/ARS"
response_tipo_cambio = requests.get(url_tipo_cambio)
data_tipo_cambio = response_tipo_cambio.json()
tipo_cambio = data_tipo_cambio["rates"]["CLP"]

def convertir_a_clp(precio_ars):    
    # Convertir el precio de ARS a CLP
    precio_clp = float(precio_ars) * tipo_cambio
    return f"{round(precio_clp, 2)}"


# Leer las AppIDs y nombres desde el archivo de texto
with open('juegos.txt', 'r', encoding='utf-8') as file:
    juegos = [line.strip().split('\t') for line in file]

# Obtener las AppIDs y nombres de la lista de juegos
appids = [juego[0] for juego in juegos]
nombres = [juego[1] for juego in juegos]

# Dividir las AppIDs en lotes más pequeños
lote_size = 1000
appids_lotes = [appids[i:i+lote_size] for i in range(0, len(appids), lote_size)]
nombres_lotes = [nombres[i:i+lote_size] for i in range(0, len(nombres), lote_size)]

# Realizar las consultas por lotes y combinar los resultados
resultados = {}
count = 0
for lote_id in appids_lotes:
    lote_nombre = nombres_lotes[count]
    resultados.update(obtener_precio(lote_id,lote_nombre))
    count+=1
    print(count,"000")

# Crear un DataFrame con los resultados
df = pd.DataFrame.from_dict(resultados, orient='index')

# Exportar el DataFrame al archivo de Excel
df.to_excel('precios_juegos.xlsx', index=False)
