# func_py_generate_qr_code.py
import qrcode

def func_py_generate_qr_code(data, filename="qrcode.png"):
    qr = qrcode.make(data)
    qr.save(filename)
    return f"QR Code saved as {filename}"

print(func_py_generate_qr_code("https://example.com"))
