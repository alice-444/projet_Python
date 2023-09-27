from PIL import Image

def resize_image(width, height):
    image = Image.open("image.jpg")

    print(f"Current size: {image.size}")

    resized_image = image.resize((width, height))

    resized_image.save("image" + str(width) +".jpeg")

width = int(input("Enter width:"))
height = int(input("Enter height:"))
resize_image(width, height)