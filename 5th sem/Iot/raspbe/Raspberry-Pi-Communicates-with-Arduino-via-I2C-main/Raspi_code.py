
#  Raspberry Pi Master for Arduino Slave
#  i2c_master_pi.py
#  Connects to Arduino via I2C


from smbus import SMBus

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

numb = 1

print ("Enter 0 for ON or 1 for OFF")
while numb == 1:
    ledstate = input(">>>>   ")

    if ledstate == "1":
        bus.write_byte(addr,0x0) # switch it on
    elif ledstate == "0":
        bus.write_byte(addr,0x0) # switch it on

    else:
        numb =0
        