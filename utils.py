import socket


def send_file(socket, filename):
    print("Sending file...")
    file = readfile(filename)
    sent_file=socket.sendall(file)
    return sent_file

def readfile(filename):
    try:
        f = open(filename,"rb")
        bytes=f.read()
    except FileNotFoundError:
         logging(socket,"ERROR",-1,"SEND",f"File {filename} does not exist!")
    return bytes


def recv_file(socket, filename):
    print("Receiving file...")
    data = bytearray(1)
    bytes_read=""
    try:
        f = open("files/"+filename,"xb")
        while(len(data) > 0 and "\\n" not in data.decode()):
            data = socket.recv(4096)
            print("Recieved data packet")
            f.write(data)
        f.close()
        logging(socket,"INFO",-1,"RECV",f"Received file.")
    except FileExistsError:
        logging(socket,"ERROR",-1,"RECV",f"File {filename} already exists!")




def send_listing(socket):
    print("Sending listing...")


def recv_listing(socket):
    print("Receiving listing...")

def logging(socket,level, port, requestType, message):

    ipAdress = socket.gethostname()

    print(f"LOG [{level}]: {ipAdress}, PORT {port}, TYPE{requestType}, {message}")
