from load_image import ft_load
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import cv2

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

    bw_cropped_cv = np.array(bw_cropped_img)
    contours, _ = cv2.findContours(bw_cropped_cv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(bw_cropped_cv, contours, -1, (0, 0, 0), 2)  # Contours color: white (255)

    # Convert OpenCV image back to PIL image for display
    contour_pil_image = Image.fromarray(bw_cropped_cv)

    tmp_array = np.array(bw_cropped_img)
    print(f"New shape after slicing: {tmp_array.shape}")
    
    # add scale labels
    width, height = contour_pil_image.size

    new_width = width + 200
    new_height = height + 200
    extended_img = Image.new("RGB", (new_width, new_height), color="white")
    extended_img.paste(contour_pil_image, (100, 100))

    # Draw is for creating the drawing context
    draw = ImageDraw.Draw(extended_img)
    font = ImageFont.load_default()

    for x in range(100, new_width - 100, 50):
        draw.text((x, new_height - 75), str(x - 100), fill="black", font=font)

    for y in range(100, new_height - 100, 50):
        draw.text((60, y), str(y -100), fill="black", font=font)

    return extended_img

def main():
    # print(ft_load("animal.jpeg"))
    (ft_zoom("animal.jpeg")).show()

if __name__ == "__main__":
    main()