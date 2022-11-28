##################################################################
# Date: 26 Nov 2022                                              #
# Developer: Swapnil Mali                                        #
# Email: swapmali3@gmail.com                                     #
# telnetdriver.py: This file implements class to feature functio-#
#                  nalities for telnet connection to remote host #
#                  and run commands on remote host               #
##################################################################

import telnetlib
import re

class TelnetConnection:
    #Constructor to set initial parameters
    def __init__(self, host, user, passwd):
        self.telnetConn = None
        self.host = host
        self.username = user
        self.password = passwd
        self.prompt = user+"@[\\w\\W]+:.*\\$"

    #Function to create telnet connection with remote host
    def connect(self):
        try:
            print("========================================================")
            print("[Log]: Connecting to Host: {:>12}".format(self.host))

            self.telnetConn = telnetlib.Telnet(self.host)

            self.telnetConn.read_until(b"login: ")
            self.telnetConn.write(self.username.encode('ascii') + b"\n")

            self.telnetConn.read_until(b"Password: ")
            self.telnetConn.write(self.password.encode('ascii') + b"\n")

            print((self.telnetConn.expect([bytes(self.prompt, 'ascii')], 30)[2]).decode('ascii'))
        except:
            print("[Log]: Exception during connection")
        finally:
            pass
        print("[Log]: Connected to host")

    #Function to run command on remote host and return response
    def runCmd(self, command):
        response = ''
        try:
            self.telnetConn.write(command.encode('ascii') + b"\n")
            response = (self.telnetConn.expect([bytes(self.prompt, 'ascii')], 30)[2]).decode('ascii')
        except:
            response = "Exception occurred during command execution."
            print("[Log]: {}".format(response))
        finally:
            return response

    #Function to close connection to remote host 
    def closeConn(self):
        print("Closing connection to host {}".format(self.host))
        try:
            self.telnetConn.write(b"exit\n")
            self.telnetConn.close()
        except:
            print("[Log]: Exception during closing connection")
        finally:
            print("========================================================")

