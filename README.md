Description-----

This project is a peer-to-peer chat application built using Python and TCP sockets. Each user runs the same program, which acts as both a client and server. Users can connect using IP address and port number and send messages directly. The program supports multiple connections and real-time messaging using threads.

Files------
chat.py — Handles user commands and starts server
network.py — Handles connections and messaging
server.py — Listens for incoming connections
How to Run
---------------------------
Run the program using:
py chat.py <port>
Example:
py chat.py 5000
Run another instance:
py chat.py 5001
----------------------
Commands
help
myip
myport
connect <ip> <port>
list
send <id> <message>
terminate <id>
exit

Team Contributions-----
Fotios Bampouridis, id: 203926937
chat.py
server.py
README
planning
Mohy Elhelw, id: 204318952
network.py
Demo video

VIDEO LINK YUTUBE-- https://youtu.be/3AYPbII9IHU
