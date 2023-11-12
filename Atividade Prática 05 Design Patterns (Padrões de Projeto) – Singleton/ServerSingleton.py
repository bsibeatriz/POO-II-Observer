class SingletonServer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonServer, cls).__new__(cls)
            cls._instance.server_list = []
        return cls._instance

    def add_server(self, server):
        if (server.startswith("http") or server.startswith("https")) and server not in self.server_list:
            self.server_list.append(server)
            return True
        else:
            return False

    def get_http_servers(self):
        return [server for server in self.server_list if server.startswith("http")]

    def get_https_servers(self):
        return [server for server in self.server_list if server.startswith("https")]


server = SingletonServer()
print(server.add_server("http://example.com"))  
print(server.add_server("https://example.com"))  
print(server.add_server("http://example.com"))  
print(server.add_server("example.com"))  
print(server.get_http_servers())  
print(server.get_https_servers())  
