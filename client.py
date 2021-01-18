import sys
import socket
import utils
args = sys.argv[1:]

hostname = args[0]
port = args[1]
operation = args[2]
if len(args)>3:
    filename = args[3]



debug = True


soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)



soc.connect((hostname,int(port)))

if operation.lower()=="put":
    fileSendResult = utils.send_file(soc,filename,"put")
if operation.lower()=="get":
    message = f"get,{filename},|"
    soc.sendall(str.encode(message))

    data = bytearray(1)
    bytes_read=""
    while len(data)>0 and "\\n" not in data.decode():
         data = soc.recv(4096)
         print("Recieved data packet")
         bytes_read+=data.decode()
         print(data)
    print("Recieved all data from server")
    print(bytes_read)
    if len(bytes_read)>0:
        data_args = bytes_read.split(",")
        print(data_args)
        print(f"Properties:[command:{data_args[0]}],[filename:{data_args[1]}]")
        print("Saving file...")
        utils.save_to_file(data_args[2],"client"+data_args[1])

if operation.lower()=="list":
    message = f"list|"
    soc.sendall(str.encode(message))

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

utils.logging(port, operation.lower(), data_args[1])

exit(0)