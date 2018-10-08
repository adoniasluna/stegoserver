import socket
from time import sleep

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = '127.0.0.1'
PORT = 12346
soc.connect((IP, PORT))


def insert_image(image, msg):
    """
    Send the image values and the message to be hidden to the server

    :param image:
        int list
    :param msg:
        string
    :return: None
    """
    code_operation = '1'.encode('utf8')
    soc.sendall(code_operation)
    sleep(0.1)
    soc.sendall(image)
    sleep(0.1)
    soc.sendall(msg)
    stego_image = soc.recv(4096)
    return list(stego_image)


def extract_msg(image):
    """
    Send only the image to the server, and wait for the message to be sent back to us
    :param image: int list

    :return: None
    """
    code_operation = '0'.encode('utf8')
    soc.sendall(code_operation)
    sleep(0.1)
    soc.sendall(image)
    sleep(1)
    msg = soc.recv(4096)
    return msg
