import socket

class Resolver:
    
    def __init__(self):
        self._cache = {}
    
    def __call__(self, host):
            self._cache[host] = socket.gethostbyname(host)
            return self._cache
    
    def clear(self):
        self._cache.clear()
        
    def has_host(self, host):
        return host in self._cache