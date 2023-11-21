from pyzbar.pyzbar import decode
from PIL import Image  # PIL-python imaging library

img = Image.open('qrcode.png')
decoded_objects = decode(img)

if decoded_objects:
    for obj in decoded_objects:
        print(f"Data: {obj.data.decode('utf-8')}")
else:
    print("No QR code found in the image.")
