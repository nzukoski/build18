from fabric.api import *

env.user = ""
env.password = ""

remote_hosts = ["unix1.andrew.cmu.edu", "unix2.andrew.cmu.edu", "unix3.andrew.cmu.edu"]

def run_command(command):
    retString = ""
    print "command to run: " + command
    for cur_host in remote_hosts:
        print "running on host " + cur_host
        env.host_string = cur_host
        out = str(run(command))
        print "output recieved"
        retString += (cur_host + ": " + out + "\n")
        print "result: " + out

    return retString

run_command("uptime")
run_command("whoami")