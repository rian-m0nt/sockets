import sys
import socket
import utils
command=""
args = sys.argv[1:]

hostname = args[0]
port = args[1]
operation = args[2]
if len(args)>3:
    filename = args[3]
    command = f"{operation},{filename}"
else:
    command = f"{operation}"

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)



soc.connect((hostname,int(port)))

soc.sendall(str.encode(command))
if operation.lower()=="put":

    utils.send_file(soc,filename)
if operation.lower()=="get":
   utils.recv_file(soc,filename)

if operation.lower()=="list":
    data=bytearray(1)
    bytes_read=""
    while len(data)>0 and "\\n" not in data.decode():
         data = soc.recv(4096)
         print("Recieved data packet")

         bytes_read+=data.decode()

    print("Recieved all data from server")

    items = bytes_read.split("\\n")

    for item in items:
        print(item)



exit(0)
