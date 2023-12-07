from PIL import Image
import numpy as np

def ft_load(path: str):
    img = Image.open(path)
    print(f"Image format: {img.format}")
    img_array = np.array(img)
    print(f"The shape of image is: {img_array.shape}")
    return img_array