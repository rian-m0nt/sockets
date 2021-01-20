import socket
import sys
import utils
import os

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

            data = client.recv(20)
            utils.logging(socket,"INFO",port,"REQUEST","Recieved data packet")
            bytes_read+=data.decode()
            utils.logging(socket,"INFO",port,"REQUEST","Recieved command data")
            print(bytes_read)


            data_args = str(bytes_read).split(",")

            print(f"Properties:[command:{data_args[0]}]")
            command = data_args[0].lower()
            if command=="put":
                print(f"INFO: Properties:[command:{data_args[0]}],[filename:{data_args[1]}]")
                utils.logging(socket,"INFO",port,"PUT","Beginning file recieve")
                file = utils.recv_file(client,data_args[1])

                break
            if command=="get":
                print(f"Properties:[command:{data_args[0]}],[filename:{data_args[1]}]")
                 #  file = utils.readfile(data_args[1])
                utils.send_file(client,data_args[1])
            if command=="list":
                print(f"Properties:[command:{data_args[0]}]")
                utils.logging(socket,"INFO",port,"LIST","Recieved list")
                files=os.listdir()
                message=""
                for file in files:
                    message += file + "\\n"
                client.sendall(str.encode(message))

            else:
                break

    finally:
        client.close()

utils.logging(port, command, data_args[1])
soc.close()
exit(0)

