from PIL import Image
import numpy as np

def ft_invert(array) -> np.ndarray:
    inverted_img_array = 255 - array
    print(f"The shape of the image after inversion: {inverted_img_array.shape}")
    print(inverted_img_array)
    inverted_img = Image.fromarray(inverted_img_array.astype('uint8'), 'RGB')
    inverted_img.show()
    return inverted_img_array


# red: index 0, green: index 1, blue: index 2
def ft_red(array) -> np.ndarray:
    red_filter = array.copy()
    # all pixel values in the green channel (index 1) are set to zero
    # for every pixel in the image
    red_filter[:, :, 1] = 0
    # same with blue (index 2)
    red_filter[:, :, 2] = 0
    red_filtered_img = Image.fromarray(red_filter)
    red_filtered_img.show()
    return red_filter

def ft_green(array) -> np.ndarray:
    green_filter = array.copy()
    green_filter[:, :, 0] = 0
    green_filter[:, :, 2] = 0
    green_filtered_img = Image.fromarray(green_filter)
    green_filtered_img.show()
    return green_filter

def ft_blue(array) -> np.ndarray:
    blue_filter = array.copy()
    blue_filter[:, :, 0] = 0
    blue_filter[:, :, 1] = 0
    blue_filtered_img = Image.fromarray(blue_filter)
    blue_filtered_img.show()
    return blue_filter

def ft_grey(array) -> np.ndarray:
    img = Image.fromarray(array)
    grey_filtered_img = img.convert('L')
    grey_filtered_img.show()
    grey_array = np.array(grey_filtered_img)
    return grey_array