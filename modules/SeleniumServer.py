import getopt
import os.path
import signal
import socket
import subprocess
import sys
import time

def have_server():
    # check that the server is running
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(">>Checking for Selenium")
        s.connect(("localhost", 4444))
        s.close()
        print(">>>Selenium Server is running")
        return True
    except socket.error as e: # Connection Refused
        print(">>>Selenium Server -- connection refused")
        return False
        
def start_server():
    print(">>>Starting Selenium Server")
    s = subprocess.Popen(['java', '-jar', 'third_party/selenium/selenium-server-standalone-2.42.2.jar'], 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.STDOUT).pid
    pidfile = open("third_party/selenium/server.pid", "w")
    pidfile.write(str(s))
    pidfile.close()
    print(">>>Selenium Server started (Process ID = " + str(s) + ")")
    
    # make sure the server is actually up
    server_up = False
    waiting = 0
    while server_up == False and waiting < 60:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("localhost", 4444))
            s.close()
            server_up = True
        except socket.error:
            time.sleep(1)
            waiting += 1

    return server_up
    
def stop_server():
    dead = False
    print(">>>Checking for third_party/selenium/server.pid file in " + os.getcwd())
    if os.path.exists("third_party/selenium/server.pid"):
        print(">>>server.pid exists")
        pidfile = open("third_party/selenium/server.pid", "r")
        pid = int(pidfile.read())
        print(">>Selenium Server is being shut down (Process ID = " + str(pid) + ")")
        pidfile.close()
        os.kill(pid, signal.SIGTERM)
        os.remove("third_party/selenium/server.pid")
        print(">>>Selenium Server has shut down")
        dead = True
    else:
        print(">>>server.pid not found")
        
    return dead

def help():
    print("monkey")

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "csk", ["check", "start", "stop"])
    for o, a in opts:
        if o == "--check":
            up = have_server()
            if up == True:
                sys.exit(0)
            else:
                sys.exit(1)
        elif o == "--start":
            up = start_server()
            if up == True:
                sys.exit(0)
            else:
                sys.exit(1)
        elif o == "--stop":
            up = stop_server()
            if up == True:
                sys.exit(0)
            else:
                sys.exit(1)

    help()
            