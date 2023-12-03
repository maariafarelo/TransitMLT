import requests
import json

def obtener_datos_ruta(coordenadas_origen, coordenadas_destino):
    # Define la URL de la API y tu código de autorización
    url_api = "https://journey-service-int.api.sbb.ch/v3/trips/by-origin-destination"
    codigo_autorizacion = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJjMTFmYTZiMS1lZGFiLTQ1NTQtYTQzZC04YWI3MWIwMTYzMjUiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vMmNkYTVkMTEtZjBhYy00NmIzLTk2N2QtYWYxYjJlMWJkMDFhL3YyLjAiLCJpYXQiOjE3MDE1ODU3MDEsIm5iZiI6MTcwMTU4NTcwMSwiZXhwIjoxNzAxNTg5NjAxLCJhaW8iOiJFMlZnWUZqNVFMSXg0cnlkaUpXZDRaNERIQ3dMbEdzY05PdjZWMFY4TCs1a2xkR0pVUVFBIiwiYXpwIjoiZjEzMmEyODAtMTU3MS00MTM3LTg2ZDctMjAxNjQxMDk4Y2U4IiwiYXpwYWNyIjoiMSIsIm9pZCI6IjM0YmYxYzU3LTgyZTktNDkxNy1iZDI0LTNjOWRlNDBmNThlYyIsInJoIjoiMC5BWUlBRVYzYUxLendzMGFXZmE4YkxodlFHckdtSDhHcjdWUkZwRDJLdHhzQll5V0NBQUEuIiwicm9sZXMiOlsiYXBpbS1kZWZhdWx0LXJvbGUiXSwic3ViIjoiMzRiZjFjNTctODJlOS00OTE3LWJkMjQtM2M5ZGU0MGY1OGVjIiwidGlkIjoiMmNkYTVkMTEtZjBhYy00NmIzLTk2N2QtYWYxYjJlMWJkMDFhIiwidXRpIjoiU1NlNXVHM25oRXlmczFfcWlrQUZBQSIsInZlciI6IjIuMCJ9.cgZOjN5J1tKw0rF28K3tnOWM4Pv6nfyG4o6abNqElbFkFbVGJVBLOrEc-H_ha10BKEevuzoZHCmr2K5KNKyiSvoLAhZo22vphFqbk93vCg2yYMiAJrywRkh0SKLXn1xn0EPcgSuIAcJ2FVcRQZ0ozx3_bnlZCMKsVRylcX8MhckweI-upLawE9Jl3nlrDay0AsAKIynmZvvsq-PbFm9xK2stvfZ79fDb6b9kPlTxETbWpmmT6J1D_2Wa5uikZ4HPMFsgf3xM3K6xaMn7vH3OfzkXiztsPU_otoTGyRpWedaTwIrqT6UD4CKQ0Yi5TVMISn8maAX1nC_783R-zY0JHg"
    # Convierte las coordenadas de origen y destino de cadenas JSON a objetos Python
    origen = json.loads(coordenadas_origen)
    destino = json.loads(coordenadas_destino)

    # Define los parámetros de la solicitud
    body = json.dumps({
        #"origin": "[7.453596,46.935511]",
        #"destination": "[7.450046,46.965716]",
        "origin": "[7.484149,46.948001]",
        "destination": "[8.537218,47.381957]",
        "date": "2023-12-18",
        "time": "13:07"
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
                    numeros = str(int(numeros) + int(numMins))
                    
                else:
                    for i in temporal:
                        if i.isdigit():
                            numeros += i
                
                durations.append(int(numeros))
                #print(durations)

            minim = min(durations)
            #print("EL minim es", minim)
            pos = durations.index(minim)
            return "L'opció més curta és la " + str(pos + 1) + " perquè té una durada de " + str(minim) + " minuts"

            #return respuesta.json().get("trips")[0].get("duration")
        else:
            # La solicitud falló, imprime el código de estado y el mensaje de error
            print(f"Error en la solicitud: {respuesta.status_code} - {respuesta.text}")
    except Exception as e:
        print(f"Error en la solicitud: {e}")


# Ejemplo de uso
coordenadas_origen = "[7.453596,46.935511]"
coordenadas_destino = "[7.450046,46.965716]"
datos_ruta = obtener_datos_ruta(coordenadas_origen, coordenadas_destino)

# Ahora puedes trabajar con los datos de la ruta obtenidos de la API
print(datos_ruta)
