# referenced from https://southcentralus.dev.cognitive.microsoft.com/docs/services/Custom_Vision_Prediction_3.0/operations/5c82db60bf6a2b11a8247c15
import http.client, urllib.request, urllib.parse, urllib.error, base64
import os

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Prediction-key': '72ac80a59962400a89997cbfd1280426',
}

params = urllib.parse.urlencode({
    # Request parameters
    'application': 'jpg',
})

try:
    img = open('/Users/stevenluong/PycharmProjects/azure_vision_caller/venv/IMG_4107.jpg', 'rb').read()
    conn = http.client.HTTPSConnection('westus2.api.cognitive.microsoft.com')
    conn.request("POST", "/customvision/v3.0/Prediction/d758f33a-f26a-400e-ad1a-f5736be20b13/detect/iterations/Iteration1/image", img, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

###################################