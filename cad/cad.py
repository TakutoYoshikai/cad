import argparse
from lina import lina
from PIL import Image

def guess_image_size(n):
    for i in range(1, int(n / 2) + 1):
        for j in range(1, i):
            if i * j == n:
                return (i, j)

def img_to_binary(imgpath, outputpath):
    image = Image.open(imgpath)
    width, height = image.size
    result_binary = ""
    for row in range(height):
        for col in range(width):
            pixel = image.getpixel((col, row))
            if image.mode == "RGBA":
                pixel = pixel[:3]
            for i in range(3):
                color = pixel[i]
                byte = lina.message_to_binary(color)
                result_binary += byte
    output_file = open(outputpath, "wb")
    output_file.write(lina.split(result_binary))
    output_file.close()
    image.close()

def binary_to_img(binarypath, outputpath):
    binary_file = open(binarypath, "rb")
    binary = binary_file.read()
    binary_file.close()
    width, height = guess_image_size(int(len(binary) / 3))
    image = Image.new("RGB", (width, height), (0, 0, 0))
    c = 0
    for row in range(height):
        for col in range(width):
            rgb = []
            for c in range(3):
                color = binary[(row * width + col) * 3 + c]
                rgb.append(color)
            image.putpixel((col, row), (rgb[0], rgb[1], rgb[2]))
    image.save(outputpath)
    image.close()




def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("mode", help="i2b or b2i")
    parser.add_argument("-i", "--input")
    parser.add_argument("-o", "--output")
    args = vars(parser.parse_args())
    if args["mode"] == "i2b":
        if args["input"] == None or args["output"] == None:
            parser.print_help()
            return
        img_to_binary(args["input"], args["output"])
    elif args["mode"] == "b2i":
        if args["input"] == None or args["output"] == None:
            parser.print_help()
            return
        binary_to_img(args["input"], args["output"])
    else:
        parser.print_help()
    
if __name__ == "__main__":
    main()
