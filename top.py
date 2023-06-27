import requests

def obtener_lista_juegos():
    url = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        juegos = data['applist']['apps']
        with open('juegos.txt', 'w', encoding='utf-8') as file:
            for juego in juegos:
                appid = juego['appid']
                nombre = juego['name']
                if nombre is not None and nombre != "":
                    file.write(f"{appid}\t{nombre}\n")
        print('La lista de juegos se ha guardado en juegos.txt.')
    else:
        print('Error al obtener la lista de juegos.')

# Ejemplo de uso
obtener_lista_juegos()
