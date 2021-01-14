import socket
import sys
import utils


args=sys.argv[1:]
port=args[0]
print("Initialising server on port: {"+port+"}")
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

soc.bind((socket.gethostname(),int(port)))
print("Successfully bound to socket: { hostname:"+socket.gethostname()+"}, {port: "+port+"}")
print("Server initialised, beginning listening...")
soc.listen(5)

while True:
    try:
        (client, address) = soc.accept()
        client_address = str(address)

        print("Established connection with " + client_address)

        while True:
            data = bytearray(1)
            bytes_read=''
            while len(data) > 0 and "|" not in data.decode():
                data = client.recv(4096)
                print("Recieved data packet")
                bytes_read+=data.decode()
            print("Recieved all data from client")
            print(bytes_read)
            if len(bytes_read)>0:
                data_args = str(bytes_read).split(",")
                print(data_args)
                print(f"Properties:[command:{data_args[0]}]")

                if data_args[0].lower()=="put":
                    print(f"Properties:[command:{data_args[0]}],[filename:{data_args[1]}]")
                    print("Saving file...")
                    utils.save_to_file(data_args[2],data_args[1])
                    break
                if data_args[0].lower()=="get":
                    print(f"Properties:[command:{data_args[0]}],[filename:{data_args[1]}]")
                  #  file = utils.readfile(data_args[1])
                    utils.send_file(client,data_args[1],"")
            else:
                break

    finally:
        client.close()

soc.close()
exit(0)

