import requests
from datetime import datetime

api_key = "2ab23cb005d34cc2df4a271708085911"  
ciudad = "campana"
url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"


respuesta = requests.get(url)


if respuesta.status_code == 200:
    datos = respuesta.json()  
    
    temperatura = datos['main']['temp']
    descripcion = datos['weather'][0]['description']
    humedad = datos['main']['humidity']
    latitud = datos['coord']['lat']
    longitud = datos['coord']['lon']
    clima_principal = datos['weather'][0]['main']
    descripcion_clima = datos['weather'][0]['description']
    icono_clima = datos['weather'][0]['icon']
    temperatura = datos['main']['temp']
    sensacion_termica = datos['main']['feels_like']
    temperatura_min = datos['main']['temp_min']
    temperatura_max = datos['main']['temp_max']
    presion = datos['main']['pressure']
    humedad = datos['main']['humidity']
    visibilidad = datos['visibility']
    velocidad_viento = datos['wind']['speed']
    direccion_viento = datos['wind']['deg']
    nubosidad = datos['clouds']['all']
    hora_actualizacion = datos['dt']
    fecha=datetime.fromtimestamp(hora_actualizacion)
    pais = datos['sys']['country']
    salida_del_sol = datos['sys']['sunrise']
    puesta_del_sol = datos['sys']['sunset']
    zona_horaria = datos['timezone']
    
    print("fecha y hora:",fecha)
    print("direccionviento:",direccion_viento)
    print("viento:",velocidad_viento)
    print(f"Clima en {ciudad}:")
    print(f"Temperatura: {temperatura}°C")
    print(f"Descripción: {descripcion.capitalize()}")
    print(f"Humedad: {humedad}%")
else:
    print("Error al obtener los datos:", respuesta.status_code)



    
    crear_pdf("reporte.pdf")