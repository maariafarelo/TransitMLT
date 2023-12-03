import requests
import json
from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS

ahora = datetime.now()
# Formatea la hora en formato de 24 horas (HH:MM)
hora_actual = ahora.strftime("%H:%M")
# print(hora_actual)
today = datetime.now()
fecha_hora_actual = ahora.strftime("%Y-%m-%d")

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def obtener_datos_ruta():
    origen = request.args.get('origen')
    destino = request.args.get('destino')
    # Define la URL de la API y tu código de autorización
    url_api = "https://journey-service-int.api.sbb.ch/v3/trips/by-origin-destination"
    codigo_autorizacion = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJjMTFmYTZiMS1lZGFiLTQ1NTQtYTQzZC04YWI3MWIwMTYzMjUiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vMmNkYTVkMTEtZjBhYy00NmIzLTk2N2QtYWYxYjJlMWJkMDFhL3YyLjAiLCJpYXQiOjE3MDE1OTY1NTUsIm5iZiI6MTcwMTU5NjU1NSwiZXhwIjoxNzAxNjAwNDU1LCJhaW8iOiJFMlZnWUZDWlZmK3JPZE13WlYvK2wzVTZyVGZ0WHQ1YjhlT0dmbXd6MzVOVHR0N3U0bjRBIiwiYXpwIjoiZjEzMmEyODAtMTU3MS00MTM3LTg2ZDctMjAxNjQxMDk4Y2U4IiwiYXpwYWNyIjoiMSIsIm9pZCI6IjM0YmYxYzU3LTgyZTktNDkxNy1iZDI0LTNjOWRlNDBmNThlYyIsInJoIjoiMC5BWUlBRVYzYUxLendzMGFXZmE4YkxodlFHckdtSDhHcjdWUkZwRDJLdHhzQll5V0NBQUEuIiwicm9sZXMiOlsiYXBpbS1kZWZhdWx0LXJvbGUiXSwic3ViIjoiMzRiZjFjNTctODJlOS00OTE3LWJkMjQtM2M5ZGU0MGY1OGVjIiwidGlkIjoiMmNkYTVkMTEtZjBhYy00NmIzLTk2N2QtYWYxYjJlMWJkMDFhIiwidXRpIjoidmdEZXdZQXBOMC1IdmNQbGVQUUdBQSIsInZlciI6IjIuMCJ9.dRhf5A6nqGTmmz7LgZwZ9TKM1E2QyyvNgde6cJlsfLBiBUBxvwPX7jzNFTlpbV7pUc23f_j4vfcI0DoyYo_EkB7_SmTR7gV8ihbYGKYOi4vu1o7mWwDoeYjRJ88csQzoEw_6e26DTPeUDMop50TvR9Z-2jtKI6DPkRjXivikZ0xjKON4RLwTfx5-sB0Y6hDOlQhb7cR_bgTvEdharOg-h0m9nRnDQW6O8BqltK-Xe3G9L6g61dxUzReoCh_tOIF4eZenHHGeAWKNt-94q5vejfmXMxPI_g16uaw5vMnv3CKvyj5p87tGtnZ5-vDxvW3QayhbGU4e1dFkwdbeR2jyOg"
    # Convierte las coordenadas de origen y destino de cadenas JSON a objetos Python
    # origen = json.loads(origen)
    # destino = json.loads(destino)

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
                    if numeros == '':
                        numeros = '0'
                    elif numMins == '':
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

            return jsonify({'option'; pos, 'duration': minim})
            # print(durations)
            # return "L'opció més curta és la " + str(pos) + " perquè té una durada de " + str(minim) + " minuts"

            #return respuesta.json().get("trips")[0].get("duration")
            #return jsonify(respuesta.json().get("trips")[pos], 200)
            #return jsonify({'message': 'croqueta'}), 200
        else:
            # La solicitud falló, imprime el código de estado y el mensaje de error
            # return jsonify({'message': 'croque'}), 404
            return jsonify({'message': f'Error en la solicitud: {respuesta.status_code} - {respuesta.text}'}), respuesta.status_code
    except Exception as e:
        return jsonify({'message': 'No route found'}), 404

