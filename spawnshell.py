
import pexpect


# input = ""
output = ""


p = pexpect.spawn("sh")

while True: 
# Establish connection with client. 
  inp = input("Enter a command: ")
  print("Input received " + inp)
  p.sendline(inp)
  out = p.buffer
  print("Output prepared  " + out.decode())

    
