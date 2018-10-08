from PIL import Image


def extracting_blue(filepath):

    """Reads an image in the specified loaction

    :returns A list of Blue values, as ints"""

    img = Image.open(filepath)
    width = img.size[0]
    height = img.size[1]
    blue_list = []

    for y in range(0, height):
        for x in range(0, width):
            _, _, b = img.getpixel((x, y))
            blue_list.append(b)
    return blue_list


def write_image(filepath, values_list):
    """Writes a new image to the same path as the original one, prepending 'encoded' to it's name

    :returns None"""

    img = Image.open(filepath)
    width = img.size[0]
    height = img.size[1]
    rgb_list = []

    for y in range(0, height):
        for x in range(0, width):
            r, g, _ = img.getpixel((x, y))
            rgb_list.append((r, g, values_list[x + (width * y)]))

    image_to_write = Image.new(img.mode, (width, height))
    image_to_write.putdata(rgb_list)
    image_to_write.save('encoded' + filepath)