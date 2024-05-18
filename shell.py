
import subprocess

port = 80

# input = ""
output = ""


p = subprocess.Popen("sh" , shell=True,stderr=subprocess.PIPE, stdin=subprocess.PIPE , stdout=subprocess.PIPE)
  

while True: 
# Establish connection with client. 
  inp = input("Enter a command: ")
  print("Input received " + inp)
  out , err = p.communicate(input= inp.encode())
  print("Output prepared  " + out.decode())
  print("Error prepared  " + err.decode())

    
