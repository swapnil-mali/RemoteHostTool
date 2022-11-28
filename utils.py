##################################################################
# Date: 26 Nov 2022                                              #
# Developer: Swapnil Mali                                        #
# Email: swapmali3@gmail.com                                     #
# utils.py: This file contains supportive function to read host  #
#           information and process response generated after a   #
#           command ifconfig                                     #
##################################################################

import re

#Generator function to read host login details
def read_hosts():
    with open('remote_hosts.csv', 'r') as host_reader:
        print(host_reader.readline())
        while True:
            line = host_reader.readline()
            if not line:
                break
            hostinfo = line.split(',')
            yield hostinfo[0].strip(), hostinfo[1].strip(), hostinfo[2].strip()

#Function to extract interface and ipaddress from response
def find_iface(response):
    host_iface = {}
    lines = response.splitlines()
    interface = ''
    ipaddress = ''
    for line in lines:
        if ": flag" in line:
            interface = (re.findall("(\w+):", line)[0])
        if "        inet " in line:
            ipaddress = (re.findall("inet (\d\d*\d*\.\d\d*\d*\.\d\d*\d*\.\d\d*\d*)", line)[0])
            host_iface.update({interface: ipaddress})
            interface = ''
            ipaddress = ''
    return host_iface
