##################################################################
# Date: 26 Nov 2022                                              #
# Developer: Swapnil Mali                                        #
# Email: swapmali3@gmail.com                                     #
# get_host_iface.py: This is main script to gather remote hosts  #
#                    network interface information               #
##################################################################

import utils
from telnetdriver import TelnetConnection

remote_iface = dict()

#Function to travers through all remote hosts, connect and extract
#network interface information
def get_host_iface():
    for hostname, username, password in utils.read_hosts():
        remote_iface[hostname] = {}
        response = ''
    
        #print(hostname, username, password)

        hostConn = TelnetConnection(hostname, username, password)
        hostConn.connect()
    
        response = hostConn.runCmd("ifconfig")
        print(response)
    
        hostConn.closeConn()
        del(hostConn)

        remote_iface[hostname] = utils.find_iface(response)


#Function to write network information to csv file
def write_iface_to_csv():
    with open("host_iface_info.csv", 'w') as writer:
        writer.writelines("Host,Interface,Ipaddress\n")
        for host in remote_iface.keys():
            for iface, ip in remote_iface[host].items():
                writer.writelines(host+","+iface+","+ip+"\n")

get_host_iface()
write_iface_to_csv()
print(remote_iface)

