import socket
#Set the max timeout (corresponds to filesize, in this case no file over 100kb can be sent)
MAX_TIMEOUT = 24
DELIMITER=","

def send_file(socket, filename,appender):
    print("Sending file...")
    file = readfile(filename)
    message = appender + DELIMITER + filename + DELIMITER + file
    sent_file=socket.sendall(str.encode(message))
    return sent_file

def readfile(filename):
    f = open(filename)
    bytes=f.read()
    return bytes


def recv_file(socket, filename):
    print("Receiving file...")
    data = bytearray()
    bytes_read=""
    timeout=0
    while(len(data) > 0 and timeout < MAX_TIMEOUT):
        data = socket.recv(4096)
        print("Recieved data packet")
        bytes_read+=data.decode()
        timeout+=1
    save_to_file(data,filename)

def save_to_file(data,filename):
    print("Saving file")
    f = open("storage/"+filename,"w")
    f.write(data)
    f.close()

def send_listing(socket):
    print("Sending listing...")


def recv_listing(socket):
    print("Receiving listing...")

