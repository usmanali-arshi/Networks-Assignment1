import sys
# TODO: import socket libraries
from socket import * 

NUM_TRANSMISSIONS=200
if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " relay_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
relay_port=int(sys.argv[1])

# TODO: Create a relay socket to listen on relay_port for new connections
relay_sock = socket(AF_INET, SOCK_STREAM)

# TODO: Bind the relay's socket to relay_port
relay_sock.bind(("127.0.0.1", relay_port))

# TODO: Put relay's socket in LISTEN mode
relay_sock.listen()
# TODO: Accept a connection first from sender.py (accept1)
(sender_socket, sender_addr) = relay_sock.accept()
# TODO: Then, accept a connection from receiver.py (accept2)
(receiver_socket, receiver_addr) = relay_sock.accept()
# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # TODO: Receive data from sender socket (the return value of accept1)
  data1 = sender_socket.recv(200).decode().strip()
  # Be careful with the length of data you receive


  # TODO: Check for any bad words and replace them with the good words
  # bad_words= ['virus', 'worm', 'malware']
  # good_words = ['groot', 'hulk', 'ironman']
  # print("HELOOOOOO")
  # for j in range(3):

  # Replace 'virus' with 'groot'
  if 'virus' in data1:
    data1 = data1.replace('virus', 'groot')

  # Replace 'worm' with 'hulk'
  if 'worm' in data1:
    data1 = data1.replace('worm', 'hulk')
  # Replace 'malware' with 'ironman'
  if 'virus' in data1:
    data1 = data1.replace('malware', 'ironman')
    # print("hello ", i)
    # if bad_words[j] in data1:
      # print("FOR TRANSMISSION", i,"BAD WORD IS ", bad_words[j],"replaced with", good_words[j])
      # data1=data1.replace(bad_words[j], good_words[j])
  data1 = data1.strip()



  # TODO: and forward the new string to the receiver socket (the return value of accept2)
  receiver_socket.send(data1.strip().encode())
  # TODO: print data that was relayed
  print("relayed:")
  print(data1)

# TODO: Close all open sockets
relay_sock.close()
sender_socket.close()
receiver_socket.close()