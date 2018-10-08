import ImageOperations
import Client

#--------NÃO PRECISA MAIS DESSE ARQUIVO------------#
"""def main():
    path = "void.png"
    image = ImageOperations.extracting_blue(path)
    image_bytes = bytes(image)
    msg = 'Gabriel'
    msg_bytes = bytes(msg, 'utf8')
    extract = bytes(ImageOperations.extracting_blue('encoded' + path))

    operation = 'E'

    if operation == 'I':
        blue_values = Client.insert_image(image_bytes, msg_bytes)
        for b in blue_values:
            print(b)
        ImageOperations.write_image(path, blue_values)

    elif operation == 'E':
        msg = list(Client.extract_msg(extract))
        decoded_msg = "".join(chr(x) for x in msg)
        print(decoded_msg)

    else:
        print("Invalid Input")
        main()

if __name__ == "__main__":
    main()"""