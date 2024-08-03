import socket
def port_scanner(target, ports):
clcoding = socket.gethostbyname(target)
print(f"Scanning ftarget) ((clcoding))")
 for port in ports:
   sock = socket.socket(socket.AF_ INET, socket.SOCK STREAM)
   socket.setdefaulttimeout(1)
   result = sock.connect_ex((clcoding, port))
   if result == 0:
     print(f"Port (port): Open")
   sock.close()
 # Example usage
target = "clcoding.com"
ports [22, 80, 443, 8080]
port_scanner(target, ports)
