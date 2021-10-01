#TODO: import socket library
from socket import * 
import sys
NUM_TRANSMISSIONS=10
if(len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " server_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
server_port = int(sys.argv[1])

# TODO: Create a socket for the server
udpServer = socket(AF_INET, SOCK_DGRAM)

# TODO: Bind it to server_port 
udpServer.bind(("127.0.0.1", server_port))
# udpServer.setblocking(False)
# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # TODO: Receive RPC request from client
  # received = udpServer.recv(4096)
  received_data = udpServer.recvfrom(4096)
  received = received_data [0] # getting the message which is the prime number
  address = received_data[1] #from the byte pair getting the address

  # print("address is",address)

  # TODO: Turn byte array that you received from client into a string variable called rpc_data
  rpc_data = received.decode()
  # print(rpc_data)

  # TODO: Parse rpc_data to get the argument to the RPC.
  # Remember that the RPC request string is of the form prime(NUMBER)
  #trying to get the correct argument
  RPC = rpc_data.split('(')
  RPC = RPC[1]
  sized = len(RPC)
  int_prime = int(RPC[:sized-1])



  # TODO: Print out the argument for debugging
  print("argument is", int_prime)

  # TODO: Compute if the number is prime (return a 'yes' or a 'no' string)
  #write a prime checking function

  if int_prime <= 1:
    ret_string = 'no'
  else:
    for i in range(2, int(int_prime/2)+1 ):
      if(int_prime % i) == 0:
        ret_string = 'no'
        break
    else:
      ret_string = 'yes'
  # print(ret_string)



  

  # TODO: Send the result of primality check back to the client who sent the RPC request
  
  udpServer.sendto(ret_string.encode(), address)


# TODO: Close server's socket
udpServer.close()