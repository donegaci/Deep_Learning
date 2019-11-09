import PIL
import numpy as np

def parse_position(position_str):

    if position_str[0] == '(':
        parsed = position_str.lstrip('(').rstrip(')').split(',')
    else:
        parsed = position_str.split()

    x, y, z = [np.float(id) for id in parsed]
    return x, y, z


def preprocess_image(image):
    IMAGE_WIDTH = 200
    IMAGE_HEIGHT = 66

    w, h = image.size
    image = image.crop((0, 50, w, 140))
    image = image.resize((200, 66), PIL.Image.BICUBIC)
    return image

