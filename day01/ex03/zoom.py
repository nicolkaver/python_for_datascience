from load_image import ft_load
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def ft_zoom(path: str) -> Image.Image:
    img = Image.open(path)
    # make it black and white
    bw_cropped_img = img.convert('L')

    width, height = img.size
    crop_size = (400, 400)
    left = (width - crop_size[0]) / 2
    top = (height - crop_size[1]) / 2
    right = (width + crop_size[0]) / 2
    bottom = (height + crop_size[1]) / 2

    bw_cropped_img = bw_cropped_img.crop((left, top, right, bottom))

    tmp_array = np.array(bw_cropped_img)
    print(f"New shape after slicing: {tmp_array.shape}")
    
    # add scale labels
    draw = ImageDraw.Draw(bw_cropped_img)
    width, height = bw_cropped_img.size
    font = ImageFont.truetype("arial.tff", 16)

    for x in range(0, width, 50):
        draw.text((x, height - 20), f"{x}px", fill="white", font=font)

    return bw_cropped_img

def main():
    # print(ft_load("animal.jpeg"))
    (ft_zoom("animal.jpeg")).show()

if __name__ == "__main__":
    main()