from client import Client

cli = Client('localhost', 8080)
cli.send_command('Hi')
