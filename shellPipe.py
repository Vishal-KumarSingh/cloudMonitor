import socket 
import subprocess

port = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen(5)

input = ""
output = ""


p = subprocess.Popen("sh" , shell=True, stdin=subprocess.PIPE , stdout=subprocess.PIPE)
  

while True: 
# Establish connection with client. 
  c, addr = server.accept()     
  print ('Got connection from', addr )
  inp = c.recv(1024).decode()
  print("Input received " + inp)
  p.stdin.write(inp.encode())
  output = p.stdout.read(10)
  print("Output prepared  " + output.decode())
  # send a thank you message to the client. encoding to send byte type. 
  c.send(output) 
  print("Output sent  ")
  # Close the connection with the client 
  c.close()


    
