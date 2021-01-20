import socket
#Set the max timeout (corresponds to filesize, in this case no file over 100kb can be sent)
MAX_TIMEOUT = 24
DELIMITER=","

def send_file(socket, filename):
    print("Sending file...")
    file = readfile(filename)
    sent_file=socket.sendall(file)
    return sent_file

def readfile(filename):
    f = open(filename,"rb")
    bytes=f.read()
    return bytes


def recv_file(socket, filename):
    print("Receiving file...")
    data = bytearray(1)
    bytes_read=""
    f = open("files/"+filename,"xb")
    while(len(data) > 0 and "\\n" not in data.decode()):
        data = socket.recv(4096)
        print("Recieved data packet")
        f.write(data)
    f.close()
    print("Completed recieve successfully");
    print(data);


def save_to_file(data,filename):
    print("Saving file")
    f = open("storage/"+filename,"xb")
    f.write(data)
    f.close()

def send_listing(socket):
    print("Sending listing...")


def recv_listing(socket):
    print("Receiving listing...")

def logging(socket, port, requestType, fileName):

    ipAdress = socket.gethostname()

    print("Log: ", ipAdress, port, requestType, fileName)
