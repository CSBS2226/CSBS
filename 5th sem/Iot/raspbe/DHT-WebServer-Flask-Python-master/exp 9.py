form smbus import SMBus

addr=0x8
bus=SMBus(1)

print("Enter 1 for ON or 0 for OFF")

while True:
    ledstate=input(">>>")
    
    if ledstate=="1":
        bus.write_byte(addr, 0x1)
        print("LED ON")
    
    elif ledstate=="0":
        bus.write_byte(addr, 0x0)
        print("LED OFF")
    else:
        print("Invalid input! Enter 1 or 0.")