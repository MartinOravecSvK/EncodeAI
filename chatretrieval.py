import socket
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(message)s',
                    
                    )

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'aurora_ignite'
token = 'oauth:6d7fajjgyeu1ukm72bm4qpuk929vpm'
channel = '#ninja'

sock = socket.socket()

sock.connect((server,port)) # connect socket to twitch

#send token, nickname and channel as encoded strings
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

#receiving channel messages
resp = sock.recv(2048).decode('utf-8') # 2048 - buffer size in bytes

resp

sock.close()
