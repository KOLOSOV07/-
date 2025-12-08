from PIL import Image, ImageEnhance
import os

def load_image(path):
    return Image.open(path)

def save_image(image, path, format=None):
    image.save(path, format=format)

def change_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def change_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def resize_image(image, new_width, new_height):
    return image.resize((new_width, new_height))

def get_image_info(image):
    width, height = image.size
    format = image.format
    return width, height, format

def preview_image(image):
    image.show()

if __name__ == "__main__":
    image_path = "input.jpg"  
    image = load_image(image_path)

    width, height, fmt = get_image_info(image)
    print(f"Размер: {width}x{height}, Формат: {fmt}")

    image_bright = change_brightness(image, 1.5)

    image_contrast = change_contrast(image_bright, 1.2)

    resized_image = resize_image(image_contrast, 800, 600)

    preview_image(resized_image)

    save_image(resized_image, "output.png", format="PNG")
    #для использования пишем в командой строке "python image_processing.py"
    #название изображения должно быть "input"