import socket
import sys
import LSB

host = socket.gethostbyname("127.0.0.1")
port = 12346

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket has been created")

try:
    s.bind((host, port))
except socket.error as error_msg:
    print('Bind failed. Error Code : ' + str(error_msg[0]) + ' Message ' + error_msg[1])
    sys.exit()

s.listen(10)

print("Socket listening")

conn, addr = s.accept()


def connection_insert_message():
    """
    Receive an image and a message, hide the message within the image and
    sending back to the client only the new image that contains the message

    :return: None
    """
    print("Connection OK")
    image_blue_values = conn.recv(4096)
    print("Image received")
    msg = conn.recv(1024)

    image_int = list(image_blue_values)
    msg_int = list(msg)

    # print(msg_int)
    # print(image_int)
    # print(len(image_int))

    msg_str  = ''
    for v in msg_int:
        msg_str = msg_str + str(v)

    # print(LSB.insert_message(image_int, msg_str))
    new_image_blue_values = bytes(LSB.insert_message(image_int, msg))
    conn.sendall(new_image_blue_values)
    conn.close()


def connection_extract_message():
    """
    Receive an image and extract the message hidden within
    sending back only the extracted message to he client

    :return: Nonemsg
    """
    image_blue_values = conn.recv(4096)
    extracted_message = LSB.extract_message(list(image_blue_values))
    print("Edi's method")
    print(LSB.extract_message(list(image_blue_values)))
    conn.sendall(bytes(extracted_message, 'utf8'))
    conn.close()


def main():
    operation_code_bytes = conn.recv(10)
    operation_code = operation_code_bytes.decode('utf8')

    if operation_code is '1':
        connection_insert_message()
    elif operation_code is '0':
        connection_extract_message()

    s.close

if __name__ == "__main__":
    main()