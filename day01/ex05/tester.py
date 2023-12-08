from pimp_img import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from load_image import ft_load

def main():
    array = ft_load("landscape.jpg")

    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

if __name__ == "__main__":
    main()