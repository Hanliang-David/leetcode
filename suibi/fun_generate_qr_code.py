# fun_generate_qr_code.py
import qrcode

def generate_qr_code(data, filename):
    img = qrcode.make(data)
    img.save(filename)

data = "https://www.example.com"
filename = "qrcode.png"
generate_qr_code(data, filename)
print(f"QR code generated and saved as {filename}")
