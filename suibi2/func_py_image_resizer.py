# func_py_image_resizer.py
from PIL import Image

def func_py_image_resizer(input_path, output_path, width, height):
    with Image.open(input_path) as img:
        img_resized = img.resize((width, height))
        img_resized.save(output_path)

func_py_image_resizer("input.jpg", "output.jpg", 200, 200)
