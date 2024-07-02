
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
    disk = execCMD("df -h / | awk 'NR==2 {print $5}'")
    process = execCMD("ps aux | wc -l")
    
    return {"cpu": cpu , "memory":memory , "disk": disk , "process" : process}

def getStaticSystemInformation():
    cpu = execCMD("lscpu | grep '^CPU(s):' | awk '{print $2}'")
    memory = execCMD("awk '/MemTotal/ {print $2, $3}' /proc/meminfo")
    disk =  execCMD("df --total -h --output=size | awk 'END {print $1}'")
    firewall = execCMD("sudo ufw status | grep 'Status' | awk '{print $2}'")
    return {"totalcpu":cpu , "totalmemory":memory , "totaldisk":disk , "firewall" : firewall, "usage":getSystemUsage()}

def getTaskManager():
    tasklist = execCMD("ps aux --sort=-%cpu")
    
    return tasklist
###   cpu usage top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}'
###   memory usage free | grep Mem | awk '{print $3/$2 * 100.0}'

## total memory awk '/MemTotal/ {print $2, $3}' /proc/meminfo
## free memory  

### use stress to stress the server 

### sudo apt install stress
### command is  stress --cpu $(nproc)