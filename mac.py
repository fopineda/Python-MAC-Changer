import subprocess
# allows to run commands with python
import re 
# allows to use regex

## ifconfig eth0 down
    ## shuts down the eth0 interface to modify it
## ifconfig eth0 hw ether 00:11:22:33:44:55
    ## modifies the eth0 interface with new MAC address
## ifconfig eth0 up
    ## turns on the eth0 interface again

class MAC_Changer:
    def __init__(self):
        self.MAC = ""

    def getMACAddress(self, interface):
        # run initital ifconfig to see settings
        output = subprocess.run(["ifconfig", interface], shell=False, capture_output=True)
        
        # decodes result from output
        result = output.stdout.decode('utf-8')

        # regex patturn used to find mac address from ifconfig result
        pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'

        # compiles the pattern into something re library can understands and search for it in the result
        regex = re.compile(pattern)
        match = regex.search(result)

        # outputs MAC address and sets it to the class variable
        currentMAC = match.group().split(" ")[1]
        self.MAC = currentMAC
        
        return currentMAC

    def changeMACAddress(self, interface, newMAC):
        # status print line
        print("[+] Current MAC address: {}".format(self.getMACAddress(interface)))
        
        # runs "ifconfig eth0 down" and prints out results if error occurred
        output = subprocess.run(["ifconfig", interface, "down"], shell=False, capture_output=True)
        print(output.stderr.decode('utf-8'))

        # runs "ifconfig eth0 hw ether 00:11:22:33:44:55" and prints out results if error occurred
        output = subprocess.run(["ifconfig", interface, "hw", "ether", newMAC], shell=False, capture_output=True)
        print(output.stderr.decode('utf-8'))

        # runs "ifconfig eth0 up" and prints out results if error occurred
        output = subprocess.run(["ifconfig", interface, "up"], shell=False, capture_output=True)
        print(output.stderr.decode('utf-8'))

        # status print lone
        print("[+] Updated MAC address is: {}".format(self.getMACAddress(interface)))

        return self.getMACAddress(interface)

