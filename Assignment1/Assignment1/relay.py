import sys
# TODO: import socket libraries


NUM_TRANSMISSIONS=200
if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " relay_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
relay_port=int(sys.argv[1])

# TODO: Create a relay socket to listen on relay_port for new connections

# TODO: Bind the relay's socket to relay_port

# TODO: Put relay's socket in LISTEN mode

# TODO: Accept a connection first from sender.py (accept1)

# TODO: Then, accept a connection from receiver.py (accept2)

# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # TODO: Receive data from sender socket (the return value of accept1)
  # Be careful with the length of data you receive

  # TODO: Check for any bad words and replace them with the good words
  # Replace 'virus' with 'groot'
  # Replace 'worm' with 'hulk'
  # Replace 'malware' with 'ironman'

  # TODO: and forward the new string to the receiver socket (the return value of accept2)

  # TODO: print data that was relayed

# TODO: Close all open sockets
