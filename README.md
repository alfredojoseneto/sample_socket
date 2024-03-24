# SOCKET

This a socket example that I wrote to understand how the connections between two sockets happen and to analyse through tcpdump and wireshark the process.

### How to use tcpdump into this context

We'll monitoring the loopback interface listening at port number 8000.
It's necessary to start the tcpdump before stablish the connection to collect all informations.

$ sudo tcpdump port 8000 -i lo -w /tmp/example_socket.pcap

### How to initialize que client and the server

First of all it's necessary to change the permission of the server.py and client.py
$ chmod u+x server.py client.py

Now we can open in one terminal the server
$ ./server.py

And open the client in another terminal
$ ./client.py

### Using Wireshark

After stablish the connection and sent some message through it and collect the
data using tcpdump, we analyse the data using wireshark.

$ wireshark /tmp/example_socket.pcap
