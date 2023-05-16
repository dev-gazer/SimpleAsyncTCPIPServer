import asyncio, socket, time

class Server:
    def __init__(self, ip, port, synchronous=True):
        self.ip = ip
        self.port = port
        self.synchronous = synchronous

    async def handle_client(self, client):
        loop = asyncio.get_event_loop()
        request = None
        while request != 'quit':
            request = (await loop.sock_recv(client, 255)).decode('utf8')
            if len(request) == 2:
                print(await self.start(request))
                return
            response = str(request) + '\n'
            return await loop.sock_sendall(client, response.encode('utf8'))
        client.close()

    async def run_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(8)
        self.server.setblocking(False)
        loop = asyncio.get_event_loop()
        while True:
            client, _ = await loop.sock_accept(self.server)
            loop.create_task(self.handle_client(client))

    async def resolve(self, val):
        return val

    async def receive(self, command):
        time.sleep(3)
        li = [command[0], command[1]]
        return await self.resolve(li)

    async def start(self, command):
        print("here we go")
        return await self.receive(command)
