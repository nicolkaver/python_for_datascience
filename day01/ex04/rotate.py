from load_image import ft_load, add_scales
from PIL import Image

def ft_rotate(img: Image.Image) -> Image.Image:
    width, height = img.size

    transposed_img = Image.new("RGB", (height, width))
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            transposed_img.putpixel((y, x), pixel)
    transposed_img = add_scales(width, height, transposed_img)
    transposed_img.show()

def main():
    ft_rotate(ft_load("animal.jpeg"))

if __name__ == "__main__":
    main()