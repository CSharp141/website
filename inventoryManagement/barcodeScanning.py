import requests

url = "https://barcodes1.p.rapidapi.com/"


barcodeScan = input("Scan barcode:")
querystring = {"query": barcodeScan}

headers = {
	"x-rapidapi-key": "efbe3e38f5msh2bbd242c5734e96p1c0569jsn038a5a358e9d",
	"x-rapidapi-host": "barcodes1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring).json()

description = str(response['product']['description'])
image_url = str(response['product']['images'][0])
title = str(response['product']['title'])
manufacturer = str(response['product']['manufacturer'])



print("Title: " + title)
print("Description: " + description)
print("Manufacturer: " + manufacturer)
print("Image url: " + image_url)

img_data = requests.get(image_url).content
with open(title + '.jpg', 'wb') as handler:
    handler.write(img_data)
