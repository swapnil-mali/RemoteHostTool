Preconditions:
1. Ensure that telnet works properly on machine from where this script is planned to execute
	1.1. This can be ensured by connecting to each remote host using telnet(one time activity)
2. Open remote_hosts.csv file and update file to include information of hosts

-----------------------------------------------------------------------------------------------------

How to run script:
1. Keep all 4 files(utils.py, telnetdriver.py, get_host_iface.py, remote_hosts.csv) in same folder
2. Execute script as below
	python3.10 get_host_iface.py
3. Response can be observed on terminal console as well as script generates host_iface_info.csv file
   containing remote host network interface information
