# Working version of bluetooth transfer using PyOBEX & PyBluez

from PyOBEX import client, headers
import bluetooth
import sys


file_path = 'test.txt' # my file is in the same directory so i'll just use the file name.

addr = 'D0:B1:28:98:27:B6' # Bluetooth address of the receiver.
print("Searching for OBEX service on %s" % addr)

service_matches = bluetooth.find_service(name=b'OBEX Object Push\x00', address = addr )
if len(service_matches) == 0:
    print("Couldn't find the service.")
    sys.exit()
print(service_matches)
first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"%s\" on %s" % (name, host))
c = client.Client(addr, port)
c.connect()

# uuid = "\x79\x61\x35\xf0\xf0\xc5\x11\xd8\x09\x66\x08\x00\x20\x0c\x9a\x66"
# c.connect(header_list=[headers.Target(uuid)])

with open(file_path) as f:
    contents = f.readlines()

c.put(file_path, *contents)
c.disconnect()
