import socket
import logging

server = "irc.chat.twitch.tv"
port = 6667
nickname = "datasci"
token = "oauth:r7mvo5l5peohulx0ktih2q7mj4dle0"
channel = "#ninja"

sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode("utf-8"))
sock.send(f"NICK {nickname}\n".encode("utf-8"))
sock.send(f"JOIN {channel}\n".encode("utf-8"))

resp = sock.recv(2048).decode("utf-8")
sock.close()

print(resp)