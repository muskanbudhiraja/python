import qrcode

data = "dont forget to drink water"

# way1
img = qrcode.make(data)
img.save('qrcode.png')

# way2 --more precise
qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
img1 = qr.make_image(fill_color='black', back_color='white')
img1.save('qrcode1.png')
