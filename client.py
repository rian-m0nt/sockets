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
exit(0)
