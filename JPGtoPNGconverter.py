import sys
import os
from PIL import Image, ImageFilter


def folder_exist(route):
    if os.path.isdir(route):
        return True
    return False


def remove_extension(photo):
    splitted_photo = photo.split(".")[:-1]
    return "".join(splitted_photo)

def convert_imgs(path):
    photos = os.listdir(os.getcwd() + "\\photos")

    for photo in photos:
        print("Converting " + photo + " ...")
        img = Image.open(os.getcwd() + "\\photos\\" + photo)
        photo_no_extension = remove_extension(photo)
        img.save(path + "\\" + photo_no_extension + ".png", "png")
        print("converted!\n")


def main():
    if len(sys.argv) != 2:
        print("Please enter a name for the folder that you want to create or use for the photos")
        print("Python JPGtoPNGconverter.py [folder name]")
        return
    folder_name = sys.argv[1]
    root_directory = os.getcwd()
    path = root_directory + "\\" + folder_name
    if folder_exist(path):
        convert_imgs(path)
    else:
        os.mkdir(folder_name)
        convert_imgs(path)


if __name__ == '__main__':
    main()
