from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    img = Image.open(path)
    img.show()
    print(f"Image format: {img.format}")
    img_array = np.array(img)
    print(f"The shape of image is: {img_array.shape}")
    print(img_array)
    return img_array