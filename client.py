import socket

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.tcp_socket = socket.create_connection((ip, port))

    def send_command(self, command):
        try:
            data = str.encode(command)
            self.tcp_socket.sendall(data)
        except Exception as err:
            print(err, err.args)
        finally:
            print("Message sent, closing.")
            self.tcp_socket.close()
