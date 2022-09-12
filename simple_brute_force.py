import socket
import sys
import string
import itertools


def main():
    args = sys.argv
    args = sys.argv
    if len(args) != 3:
        print("The script should be called with 2 arguments : destination address and port.")
    else:
        alphabet = list(string.ascii_lowercase)
        number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        possible_entree = alphabet + number_list
        args = sys.argv
        ip_address = str(args[1])
        port = int(args[2])
        address = (ip_address, port)
        with socket.socket() as client_socket:
            client_socket.connect(address)
            length = 1
            not_found = True
            while not_found:
                possible_entree *= length
                iter1 = itertools.combinations(possible_entree, length)
                for i in iter1:
                    data = ""
                    for j in i:
                        data += str(j)
                    data1 = data
                    client_socket.send(data.encode())
                    response = client_socket.recv(6015)
                    response = response.decode()
                    if response == "Connection success!":
                        not_found = False
                        print(data1)
                length += 1


if __name__ == '__main__':
    main()
