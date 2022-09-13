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
        args = sys.argv
        ip_address = str(args[1])
        port = int(args[2])
        address = (ip_address, port)
        with socket.socket() as client_socket:
            client_socket.connect(address)
            with open(r".\passwords.txt", 'r') as password:
                for line in password:
                    password_ = str(line.rstrip("\n"))
                    password_list = []
                    for i in password_:
                        element = ""
                        element += i
                        element += i.upper()
                        password_list.append(element)
                    for i in list(itertools.product(*password_list)):
                        data = str(''.join(i))
                        reference_data = data
                        client_socket.send(data.encode())
                        response = client_socket.recv(9090)
                        response = response.decode()
                        if response == "Connection success!":
                            print(reference_data)
                            exit(0)


if __name__ == "__main__":
    main()
