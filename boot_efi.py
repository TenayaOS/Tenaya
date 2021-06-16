from time import sleep as delay
from os import system as shell
from os import chdir

bios_name = "VGABios"
version = "1.0.2"

def window(body, raise_base, script="/non-shell.sbin"):
    ah = str(body)
    al = (script)
    for i in range(0, int(raise_base)):
        bx = ah
        with open(bx, "r") as dl:
            dl = dl.read()
            
            if dl == ah:
                break
            
            else:
                mh = i
                if mh == 10:
                    break
    return bx, al, ah, mh            
def bits(bits, base=36):
    window(body="network.py", raise_base=base)
    return bits

class TardisLoader:
    def __init__(self):
        try:
            cd = self.boot_cdRom()
            print(), delay(3)
        except KeyboardInterrupt:
            if cd == False:
                try:
                    hdd =  self.boot_Hard_Disk()
                    print(), delay(3)
                except KeyboardInterrupt:
                    if hdd == False:
                        self.boot_Network()
                else:
                    if hdd == False:
                        self.boot_Network()                
        else:
            if cd == False:
                try:
                    hdd =  self.boot_Hard_Disk()
                    print(), delay(3)
                except KeyboardInterrupt:
                    if hdd == False:
                        self.boot_Network()
                else:
                    if hdd == False:
                        self.boot_Network()   
        
    def boot_cdRom(self):
        try:
            print("Booting from CD-Rom. . ."), delay(2)
            a = open("drive\main.py")
            a.close()
        except FileNotFoundError:
            print("Boot Fail: cannot read this boot disk")
            return False
        except KeyboardInterrupt:
            return False
        else:
            input("Press ENTER to start/read CD-Rom drive. . .")
            shell("python drive\main.py")
            return True
    
    def boot_Hard_Disk(self):
        try:
            print("Booting from Hard Disk. . ."), delay(2)
            a = open("os\kernel.py")
            a.close()
        except FileNotFoundError:
            print("Boot Fail: cannot read this boot driver")
            return False
        except KeyboardInterrupt:
            return False
        else:
            chdir("os")
            shell("python kernel.py")
            return True
    
    def boot_Network(self):
        shell("python network.py")
        
def assingture(assing_key):
    shell("cls")
    if assing_key == "0x500h" or assing_key == "0x6730b":
        TardisLoader()
    return True


bits(32)
assingture("0x500h")