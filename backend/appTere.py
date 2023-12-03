import requests
import json

def obtener_datos_ruta(coordenadas_origen, coordenadas_destino):
    # Define la URL de la API y tu código de autorización
    url_api = "https://journey-service-int.api.sbb.ch/v3/trips/by-origin-destination"
    codigo_autorizacion = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJjMTFmYTZiMS1lZGFiLTQ1NTQtYTQzZC04YWI3MWIwMTYzMjUiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vMmNkYTVkMTEtZjBhYy00NmIzLTk2N2QtYWYxYjJlMWJkMDFhL3YyLjAiLCJpYXQiOjE3MDE1NjM0MTEsIm5iZiI6MTcwMTU2MzQxMSwiZXhwIjoxNzAxNTY3MzExLCJhaW8iOiJBU1FBMi84VkFBQUE1VUJBeDNwR1dtNkVvVnZmelJPam5ldTRoSkdNaEJYNDN1TnVLUlh3NGFZPSIsImF6cCI6ImYxMzJhMjgwLTE1NzEtNDEzNy04NmQ3LTIwMTY0MTA5OGNlOCIsImF6cGFjciI6IjEiLCJvaWQiOiIzNGJmMWM1Ny04MmU5LTQ5MTctYmQyNC0zYzlkZTQwZjU4ZWMiLCJyaCI6IjAuQVlJQUVWM2FMS3p3czBhV2ZhOGJMaHZRR3JHbUg4R3I3VlJGcEQyS3R4c0JZeVdDQUFBLiIsInJvbGVzIjpbImFwaW0tZGVmYXVsdC1yb2xlIl0sInN1YiI6IjM0YmYxYzU3LTgyZTktNDkxNy1iZDI0LTNjOWRlNDBmNThlYyIsInRpZCI6IjJjZGE1ZDExLWYwYWMtNDZiMy05NjdkLWFmMWIyZTFiZDAxYSIsInV0aSI6IlRyWFVGVnhiU2ttLVNYb1pUM3RHQUEiLCJ2ZXIiOiIyLjAifQ.BGwxwCm-EZS4LciX6ZVndIRFM57i7Nubfx0hhtvJeTeeUpBdOgrPz2Ts4Qaas47gmnhMJL4D_QtGMuwrg1MPg6XQPqov91wcowZUAEFKj9q3ZfuWd2ZzccwE1s0_UktUoP2IRZ2mNfNxL2D3ba8hX69VPS5AqY4zsJY1nCIW6bLK763Y4ZAmc7fPpWow0VG91STFvhVnrdpb9JesCTf3xdlqALHxlzWeQNx76oU-L9jO_M_w4XdjUmMvD4XRRNq5i_YeH25ViwQFIkCAh1dADIpDX9Qd2Fi6ly0O_DfgXZmoDbCpf6M7jmFwwjYeYBzwwnLwWCus3X3PeOmRy4cJ9w"
    # Convierte las coordenadas de origen y destino de cadenas JSON a objetos Python
    origen = json.loads(coordenadas_origen)
    destino = json.loads(coordenadas_destino)

    # Define los parámetros de la solicitud
    body = json.dumps({
        "origin": "[7.453596,46.935511]",
        "destination": "[7.450046,46.965716]",
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
                numeros = ''
                for i in temporal:
                    if i.isdigit():
                        numeros += i
                durations.append(numeros)

            minim = min(durations)
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
