from mac import MAC_Changer
# imports the mac changer class

if __name__ == "__main__":
    mc = MAC_Changer()
    mac = mc.getMACAddress("eth0")

    # runs the mac changer function
    newMAC = mc.changeMACAddress("eth0", "00:11:22:33:44:66")