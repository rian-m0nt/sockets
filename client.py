import sys
import socket
import utils
args = sys.argv[1:]

hostname = args[0]
port = args[1]
operation = args[2]
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
    while len(data)>0:
         data = soc.recv(4096)
         print("Recieved data packet")
         bytes_read+=data.decode()
    print("Recieved all data from server")
    print(bytes_read)
    data_args = bytes_read.split()
    print(f"Properties:[command:{data_args[0]}],[filename:{data_args[1]}]")
    print("Saving file...")
    utils.save_to_file(data_args[2],data_args[1]+"d")
exit(0)
