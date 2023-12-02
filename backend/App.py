from flask import Flask, request, jsonify
import requests
#app = Flask(__name__)

#api_url = "https://journey-service-int.api.sbb.ch/v3/trips/by-origin-destination"

#@app.route("/ping")
 #def ping():
    #return 'Pong!'
#data = response.json


#def hello_world(): #to tell Flask what URL should trigger our function.
  #  return "<p>Hello, World!</p>"

#if __name__ == '__main__':
#    app.run(debug=True)


def obtener_rutas(origen, destino, api_key):
    # URL de la API de OpenRouteService para obtener rutas
    url = "https://journey-service-int.api.sbb.ch/v3/trips/by-origin-destination"

    # Parámetros de la solicitud
    params = {
        "api_key": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJjMTFmYTZiMS1lZGFiLTQ1NTQtYTQzZC04YWI3MWIwMTYzMjUiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vMmNkYTVkMTEtZjBhYy00NmIzLTk2N2QtYWYxYjJlMWJkMDFhL3YyLjAiLCJpYXQiOjE3MDE1NTQ1NTUsIm5iZiI6MTcwMTU1NDU1NSwiZXhwIjoxNzAxNTU4NDU1LCJhaW8iOiJFMlZnWUNpNFVlVXZzQ041cVUvVURwNE5iYXlzMDlST0dQeGtpTlJ3M002Y3hlb3V1QThBIiwiYXpwIjoiZjEzMmEyODAtMTU3MS00MTM3LTg2ZDctMjAxNjQxMDk4Y2U4IiwiYXpwYWNyIjoiMSIsIm9pZCI6IjM0YmYxYzU3LTgyZTktNDkxNy1iZDI0LTNjOWRlNDBmNThlYyIsInJoIjoiMC5BWUlBRVYzYUxLendzMGFXZmE4YkxodlFHckdtSDhHcjdWUkZwRDJLdHhzQll5V0NBQUEuIiwicm9sZXMiOlsiYXBpbS1kZWZhdWx0LXJvbGUiXSwic3ViIjoiMzRiZjFjNTctODJlOS00OTE3LWJkMjQtM2M5ZGU0MGY1OGVjIiwidGlkIjoiMmNkYTVkMTEtZjBhYy00NmIzLTk2N2QtYWYxYjJlMWJkMDFhIiwidXRpIjoiRmp0emdyOTlkMENEdlo5RlItTUhBQSIsInZlciI6IjIuMCJ9.r_cjyi9XYtvoq8g1Katue-2UpRt5FWiHr0CRI5WkgX7ZT82wVwsmUiDtccgvV8Af9h4CIxY5j6sueF7jO7IC5b-z8cs5-CRFEIgNpCL4VfdD0WyVdf9iC3Ehxk50mXsPrnwaWV8iUNNZDPKOvNC6sXOwMt_nd0QAic9EUMJw318yx07h0I_Day9edlfdFrX4HQKyMYWzPs6B-RiQe-VNRestWjpYUg5YhSU_dECP-LdYhb7X6d8B2TvkSdnaA3AXLlOIEPhiSWd5weIRPDcgrinu3A6eVN5M7dFDHI2BDDwrbslmByqzfAUX3dA1uwUUu9JIIcCD1Cyz1Hy04JOdyw',
        "coordinates": [[origen[1], origen[0]], [destino[1], destino[0]]],
        "format": "geojson",
    }

    # Realizar la solicitud
    response = requests.post(url, json=params)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta a formato JSON
        data = response.json()
        return data
    else:
        # Imprimir un mensaje de error si la solicitud no fue exitosa
        print(f"Error en la solicitud. Código de estado: {response.status_code}")
        return None

# Ejemplo de uso
origen = [-74.006, 40.7128]  # Latitud y longitud de Nueva York (origen)
destino = [-118.2437, 34.0522]  # Latitud y longitud de Los Ángeles (destino)
api_key = "tu_clave_de_api"  # Reemplaza con tu clave de API de OpenRouteService

rutas = obtener_rutas(origen, destino, api_key)

if rutas:
    # Imprimir información de las rutas
    '''
    for i, ruta in enumerate(rutas['features']):
        print(f"Ruta {i+1}:")
        print(ruta['properties']['segments'][0]['distance'], "metros")
        print(ruta['properties']['segments'][0]['duration'], "segundos")
        print("Coordenadas:")
        print(ruta['geometry']['coordinates'])
        print("\n")

    '''