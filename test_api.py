import requests

url = "http://127.0.0.1:8000/api/taxis/"

payload = "{\r\n    \r\n    \"numero\": 1235,\r\n    \"comentario\": \"me cobro un chingoxxxxxxxxxxxxxxxxxxx\",\r\n    \"calificacion\": 1,\r\n    \"costo\": 25,\r\n    \"color\": 1\r\n}"
headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    'Postman-Token': "ca60d9d2-c48b-40b5-9867-a440f6531239",
    'Authorization': "Bearer nJsuL2Rr84PDOyIvm6DHlrFAtpNx1F",
}

response = requests.request("POST", url, data=payload, headers=headers)
#response = requests.request("GET", url, headers=headers)

print(response.text)
