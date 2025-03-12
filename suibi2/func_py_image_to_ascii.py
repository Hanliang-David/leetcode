# func_py_image_to_ascii.py
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def func_py_image_to_ascii(image_path, new_width=100):
    img = Image.open(image_path).convert("L")
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    img = img.resize((new_width, new_height))

    pixels = img.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel // 32] for pixel in pixels)
    ascii_str = "\n".join(ascii_str[i:(i+new_width)] for i in range(0, len(ascii_str), new_width))
    return ascii_str

print(func_py_image_to_ascii("image.jpg"))
