# This script is for stegonographic operations

def insert_message(blue_values, msg):
    global size_new_blue_values_in_binary
    new_blue_values_in_binary = []
    size_in_binary_msg = '{:032b}'.format(len(msg))
    msg_in_binary = size_in_binary_msg + ''.join('{:08b}'.format(x) for x in msg)
    blue_values_in_binary = ['{:08b}'.format(x) for x in blue_values]
    counter = 0

    for i in msg_in_binary:
        aux_blue_value = ''.join('{:08b}'.format(blue_values[counter]))

        if aux_blue_value[len(aux_blue_value) - 1] == i:
            counter = counter + 1
            new_blue_values_in_binary.append(aux_blue_value)

        else:
            blue_changed_in_binary = aux_blue_value[:len(aux_blue_value) - 1] + i
            new_blue_values_in_binary.append(blue_changed_in_binary)
            counter = counter + 1
            size_new_blue_values_in_binary = len(new_blue_values_in_binary)

        if counter == len(blue_values)-1:
            break

    for rest_blue_values_in_binary in blue_values_in_binary[size_new_blue_values_in_binary:]:
        new_blue_values_in_binary.append(rest_blue_values_in_binary)

    new_blue_values = [int(x, 2) for x in new_blue_values_in_binary]
    return new_blue_values


def extract_message(blue_values):
    size_msg = ''
    msg_binary = ''

    for i in blue_values:
        element_binary = '{:08b}'.format(i)
        size_msg = size_msg + element_binary[len(element_binary) - 1]
        if len(size_msg) == 32:
            break

    for x in blue_values[32:32 + ((int(size_msg, 2)) * 8)]:
        binary = '{:08b}'.format(x)
        msg_binary = msg_binary + binary[len(binary) - 1]
        msg_interger = int(msg_binary, 2)
        if len(msg_binary) == ((int(size_msg, 2)) * 8):
            msg = msg_interger.to_bytes((msg_interger.bit_length() + 7) // 8, 'big').decode('utf8', 'surrogatepass')
            return msg
