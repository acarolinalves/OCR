import cv2, io, json, requests, numpy as np

# API - Preencha sua api key e a linguagem desejada.
url_api = "https://api.ocr.space/parse/image"
apiKey = ""
language = ""

#OCR
#Substitua "eng.jpg" pela imagem que será utilizada.

img = cv2.imread('img/eng.jpg')

_, compressedimage = cv2.imencode('.jpg', img, [1, 90])
file_bytes = io.BytesIO(compressedimage)

response = requests.post(url_api, files = {"eng.jpg": file_bytes}, data = {"apikey": apiKey, "language": language})

result = json.loads(response.content.decode())
parsedResults = result.get("ParsedResults")[0]
textDetected = parsedResults.get("ParsedText")

print(textDetected)


