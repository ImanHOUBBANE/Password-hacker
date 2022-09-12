import socket
import sys


def main():
    args = sys.argv
    args = sys.argv
    if len(args) != 4:
        print("The script should be called with 3 arguments : destination address , port number  and data. ")
    else:
        args = sys.argv
        ip_address = str(args[1])
        port = int(args[2])
        address = (ip_address, port)
        data = str(args[3])
        with socket.socket() as client_socket:
            client_socket.connect(address)
            client_socket.send(data.encode())
            response = client_socket.recv(6015)
            response = response.decode()
            print(response)


if __name__ == "__main__":
    main()
