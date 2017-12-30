import sys
from pyHS100 import SmartPlug

#code modified by Jacob Thomas for use with OctoPrint -> www.github.com/tunnelsnake
print("----------------Smartplug Interface---------------- \n")

while(True):

    inp = input("Plug> ")


    if str.lower(inp) == "change":
        f = open("ip.log", "w").close()
        f = open("ip.log", "w")

        newip = input("Enter New IP Of Outlet:")
        f.write(newip)
        f.close()

        print("New IP Written.")


    f = open("ip.log", 'r')
    ip = f.readline()
    f.close()

    if ip != None:
        s = SmartPlug(ip)
        powerOn = s.is_on

    else:
        print("No ip.log File. Type 'change' to enter new ip.")


    if str.lower(inp) == "status":
        if powerOn == True:
            print("POWER Status: ONLINE ")
        else:
            print("POWER Status: OFFLINE ")

        print("Stored IP: " + ip)
        print("Alias: " + s.alias)

    elif str.lower(inp) == "on":
        if powerOn == True:
            print("Power Already On.")

        else:
            s.turn_on()
            print("Power Turned On.")

    elif str.lower(inp) == "off":
        if powerOn == False:
            print("Power Already Off.")

        else:
            s.turn_off()
            print("Power Turned On.")

    elif str.lower(inp) == "help":
        print("status - print ip and outlet status")
        print("on - turn on the outlet")
        print("off - turn off the outlet")
        print("change - change current ip")
        print("help - display this message")
        print("exit - exit this prompt")

    elif str.lower(inp) == "exit":
        exit(0)

    else:
        print("Invalid Choice - type 'help' for help ")

