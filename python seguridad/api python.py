import requests

def clima(ciudad):
    key="a8f7172e3d2448a50da55c029ea2832a"
    url="http://api.openweathermap.org/data/2.5/weather"
    parametros={"APPID":key,"q":ciudad,"units":"metric", "lang":"es","cnt":27}
    response= requests.get(url, params=parametros)
    clima=response.json()
    ciudad=clima["name"]
    descrip=clima["weather"][0]["description"]
    temp=clima["main"]["temp"]
    print("la ciudad: ",ciudad)
    print("su temperatura: ",temp," C°")
    print("descripcion: ",descrip)

ciudad=input("Ingrese la ciudad: ")
clima(ciudad)
#Dos peticiones, temperatura y descripción
