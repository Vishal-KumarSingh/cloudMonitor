import socket 
import subprocess


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost" , 9999))

print("sending the message ")
client.send("ls ".encode())

print(" message sent now starting to receive")
data = client.recv(1024)

print("Message received" + data.decode())
    
