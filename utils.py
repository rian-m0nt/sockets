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
        print(f"File {filename} not found.")

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
        print("Completed recieve successfully");
    except FileExistsError:
        print(f"File {filename} already exists!")
    print(data);



def send_listing(socket):
    print("Sending listing...")


def recv_listing(socket):
    print("Receiving listing...")

def logging(socket, port, requestType, fileName):

    ipAdress = socket.gethostname()

    print("Log: ", ipAdress, port, requestType, fileName)
