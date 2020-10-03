#!/usr/bin/python

import os
import signal
from subprocess import Popen, PIPE


def kill_processes_bind_to_port(port):
    process = Popen(["lsof", "-i", ":{0}".format(port)], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    for process in str(stdout.decode("utf-8")).split("\n")[1:]:
        data = [x for x in process.split(" ") if x != '']
        if len(data) <= 1:
            continue
        os.kill(int(data[1]), signal.SIGKILL)


def main():
    ports = [2222, 1900, 1099]
    [kill_processes_bind_to_port(_) for _ in ports]
    os.system("cd VS_LM && sh StartServer.sh & cd VS_AR && sh VisualSim.sh")


main()
