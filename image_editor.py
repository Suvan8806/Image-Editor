import sys
import os
from PIL import Image, ImageFilter

# grab the arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]


# check if new exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ask for resizer, convertor or rotator
a = int(input("Do you want a resizer, convertor or a rotator? (1,2 or 3): ")) 

# resizer
def resizer():
    x, y = map(int, input("What size would you like to resize them to? (e.g., 200 400): ").split())
    file_type = input("What image format would you like? (png, pdf, jpeg): ")
    for filename in os.listdir(image_folder):
        img = Image.open(os.path.join(image_folder, filename))
        new_img = img.thumbnail((x, y))
        clean_name = os.path.splitext(filename)[0]
        new_img.save(os.path.join(output_folder, f"{clean_name}.{file_type}"), file_type.upper())
        print("Resized!")

# convertor
def convertor():
    file_type = input("What image format would you like? (png, pdf, jpeg): ")
    for filename in os.listdir(image_folder):
        img = Image.open(f"{image_folder}{filename}")
        clean_name = os.path.splitext(filename)[0]
        img.save(os.path.join(output_folder, f"{clean_name}.{file_type}"), file_type.upper())
        print("Converted!")

# rotator
def rotator():
    x = int(input("By how many degrees would you like to rotate your image? "))
    file_type = input("What image format would you like? (png, pdf, jpeg): ")
    for filename in os.listdir(image_folder):
        img = Image.open(os.path.join(image_folder, filename))
        new_img = img.rotate(x)
        clean_name = os.path.splitext(filename)[0]
        new_img.save(os.path.join(output_folder, f"{clean_name}.{file_type}"), file_type.upper())
        print("rotated!")

# call the function
if a == 1:
    resizer()
elif a == 2:
    convertor()
elif a == 3:
    rotator()
