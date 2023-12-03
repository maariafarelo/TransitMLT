import requests
import json
from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS

ahora = datetime.now()
# Formatea la hora en formato de 24 horas (HH:MM)
hora_actual = ahora.strftime("%H:%M")
#print(hora_actual)
today = datetime.now()
fecha_hora_actual = ahora.strftime("%Y-%m-%d")


app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def obtener_datos_ruta():
    coordenadas_origen = request.args.get('origin')
    coordenadas_destino = request.args.get('destination')
    # Define la URL de la API y tu código de autorización
    url_api = "https://journey-service-int.api.sbb.ch/v3/trips/by-origin-destination"
    codigo_autorizacion = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJjMTFmYTZiMS1lZGFiLTQ1NTQtYTQzZC04YWI3MWIwMTYzMjUiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vMmNkYTVkMTEtZjBhYy00NmIzLTk2N2QtYWYxYjJlMWJkMDFhL3YyLjAiLCJpYXQiOjE3MDE1ODk3NTMsIm5iZiI6MTcwMTU4OTc1MywiZXhwIjoxNzAxNTkzNjUzLCJhaW8iOiJBU1FBMi84VkFBQUFMOC9RWWhNMmNoOTNOcHNjbnE5N1JIcEZacW5hYWRleXdPbE4xZEN0MHNNPSIsImF6cCI6ImYxMzJhMjgwLTE1NzEtNDEzNy04NmQ3LTIwMTY0MTA5OGNlOCIsImF6cGFjciI6IjEiLCJvaWQiOiIzNGJmMWM1Ny04MmU5LTQ5MTctYmQyNC0zYzlkZTQwZjU4ZWMiLCJyaCI6IjAuQVlJQUVWM2FMS3p3czBhV2ZhOGJMaHZRR3JHbUg4R3I3VlJGcEQyS3R4c0JZeVdDQUFBLiIsInJvbGVzIjpbImFwaW0tZGVmYXVsdC1yb2xlIl0sInN1YiI6IjM0YmYxYzU3LTgyZTktNDkxNy1iZDI0LTNjOWRlNDBmNThlYyIsInRpZCI6IjJjZGE1ZDExLWYwYWMtNDZiMy05NjdkLWFmMWIyZTFiZDAxYSIsInV0aSI6IlczV2I4dE5uU1VTbjVDdldTRFlGQUEiLCJ2ZXIiOiIyLjAifQ.OuX1sEhITcpGbQdgZmfYxzvzA-8z_S1OKcCpyyOSm_6sGeizlFb0OwwARmXQXHrTlOQXsFKnTzokMliQNvkAkl-AGAgzq-MueGuNlBIG9770Trmk8yfOna9sSF5gJw8q5EkPccEekc9-fp44Xoy-lj2ddcF7TKPxTk4PVfO90NC54NPyQieEQt52I-iIypeVjlWokYGlYnVkeHRZ0fLBkqFFQ0Lc5Oar3HfC91BSi6ohuLrPv6MW06xvcdD98Wim0igzOBFMUyKxhsr_5pNuqzw84JGWYQREFvBq8I8rR3k3gtltq45d_Fl_ddA5_YeicCpp51rnAfvHnIKolQaPhA"
    # Convierte las coordenadas de origen y destino de cadenas JSON a objetos Python
    origen = json.loads(coordenadas_origen)
    destino = json.loads(coordenadas_destino)

    # Define los parámetros de la solicitud
    body = json.dumps({
        "origin": origen,
        "destination": destino,
        "date": fecha_hora_actual,
        "time": hora_actual
    })

    # Define los encabezados con el código de autorización
    headers = {
        'Authorization': f'Bearer {codigo_autorizacion}',
        'Content-Type': 'application/json'  # Ajusta según los requisitos de la API
    }

    # Realiza la solicitud a la API
    try:
        respuesta = requests.post(url_api, data=body, headers=headers)

        # Verifica el estado de la respuesta
        if respuesta.status_code == 200:
            # La solicitud fue exitosa, devuelve los datos
            durations = []
            for i in range(len(respuesta.json().get("trips"))):
                temporal = respuesta.json().get("trips")[i].get("duration")
                hayH = False
                numMins = ''
                numeros = ''
                if "H" in temporal:
                    for i in temporal:
                        if i == "H":
                            hayH = True
                            numeros = str(int(numeros) * 60)
                        elif hayH == True:
                            if i.isdigit():
                                numMins += i
                        else:
                            if i.isdigit():
                                numeros += i
                    if numeros =='':
                        numeros = '0'
                    elif numMins =='':
                        numMins = '0'
                    numeros = str(int(numeros) + int(numMins))

                else:
                    for i in temporal:
                        if i.isdigit():
                            numeros += i

                durations.append(int(numeros))
                # print(durations)

            minim = min(durations)
            # print("EL minim es", minim)
            pos = durations.index(minim)
            #print(durations)
            # return "L'opció més curta és la " + str(pos) + " perquè té una durada de " + str(minim) + " minuts"

            # return respuesta.json().get("trips")[0].get("duration")
            #return jsonify(respuesta.json().get("trips")[pos], 200)
            return jsonify({'message': 'croqueta'}), 200
        else:
            # La solicitud falló, imprime el código de estado y el mensaje de error
            return jsonify({'message': 'No route found'}), 404
    except Exception as e:
        return jsonify({'message': 'No route found'}), 404


#coordenadas_origen = "[7.453596,46.935511]"
#coordenadas_destino = "[7.450046,46.965716]"
#datos_ruta = obtener_datos_ruta()

