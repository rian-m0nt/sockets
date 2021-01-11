import socket
import sys
import utils


args=sys.argv[1:]
port=args[0]
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

soc.bind((socket.gethostname(),port))

soc.listen(5)

while True:
    try:
        (client, address) = soc.accept()
        client_address = str(address)

        print("Established connection with " + client_address)

        while True:
            read = utils.recv_file(socket,)
            if read == 0:
                print("Connection with " + client_address + " has been closed.")
                break

            write = None
            if write == 0:
                print("Connection with " + client_address + " has been closed.")
                break
    finally:
        client.close()

soc.close()
exit(0)

