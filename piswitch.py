import sys
from pyHS100 import SmartPlug

#code modified by Jacob Thomas for use with OctoPrint -> www.github.com/tunnelsnake
print("----------------Smartplug Interface----------------")

if len(sys.argv) != 2:
    print("Invalid Argument. Exiting. \n")
    exit(1)


if str.lower(str(sys.argv[1])) == "change":
    f = open("ip.log", "w").close()
    f = open("ip.log", "w")

    newip = input("Enter New IP Of Outlet:")
    f.write(newip)
    f.close()

    print("New IP Written. Exiting")
    exit(0)

f = open("ip.log", 'r')
ip = f.readline()
f.close()

if ip != None:
    s = SmartPlug(ip)
    powerOn = s.is_on

else:
    print("No ip.log File. Exiting. ")
    exit(1)

if str.lower(str(sys.argv[1])) == "status":
    if powerOn == True:
        print("POWER Status: ONLINE ")
    else:
        print("POWER Status: OFFLINE ")

    print("Stored IP: " + ip)
    print("Alias: " + s.alias)
    exit(0)

elif str.lower(str(sys.argv[1])) == "on":
    if powerOn == True:
        print("Power Already On. Exiting.")
        exit(1)
    else:
        s.turn_on()
        print("Power Turned On. Exiting.")
        exit(0)

elif str.lower(str(sys.argv[1])) == "off":
    if powerOn == False:
        print("Power Already Off. Exiting.")
        exit(1)
    else:
        s.turn_off()
        print("Power Turned On. Exiting.")
        exit(0)

elif str.lower(str(sys.argv[1])) == "help":
    print("status - print ip and outlet status")
    print("on - turn on the outlet")
    print("off - turn off the outlet")
    print("change - change current ip")

else:
    print("Invalid Argument. Exiting. ")
    exit(1)

