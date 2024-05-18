
import subprocess
import threading
import time

def execCMD(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True , text=True)
    print(result.stdout)
    return result.stdout



def getSystemUsage():
    cpu = execCMD("top -bn1 | grep 'Cpu(s)' | awk '{print $2 + $4}'")
    memory = execCMD("free | grep Mem | awk '{print $3/$2 * 100.0}'")
    return {"cpu": cpu , "memory":memory}

def getStaticSystemInformation():
    cpu = execCMD("lscpu | grep '^CPU(s):' | awk '{print $2}'")
    memory = execCMD("awk '/MemTotal/ {print $2, $3}' /proc/meminfo")
    return {"totalcpu":cpu , "totalmemory":memory , "usage":getSystemUsage()}

###   cpu usage top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}'
###   memory usage free | grep Mem | awk '{print $3/$2 * 100.0}'

## total memory awk '/MemTotal/ {print $2, $3}' /proc/meminfo
## free memory  

### use stress to stress the server 

### sudo apt install stress
### command is  stress --cpu $(nproc)