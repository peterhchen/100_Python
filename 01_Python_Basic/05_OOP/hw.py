# Putting it all together: "A virtual TV"
class tvSim(object): 
    """A virtual TV """ 
    onOff = 0 
    channelNo = 2 
    volNo = 15 
    
    def __init__(self, name, onOff = 0, channelNo = 2, volNo = 15): 
        self.__name = name 
        self.onOff = onOff 
        self.channelNo = channelNo 
        self.volNo = volNo

    @property
    def name(self):
        return self.__name

    def status (self):
        print ("TV name: " + self.name + ", on/off: " + str(self.onOff) + ", channel no: " + str(self.channelNo) + ", volume: " + str (self.volNo))

    def onOffTV(self):
        if self.onOff == 0:
            self.onOff = 1
        else:
            self.onOff = 0


    def channel(self):
        channelNo = int (input ("channel no: "))
        if self.onOff == 0:
            pass
        self.channelNo = channelNo
        if self.channelNo < 2:
            self.channleNo = 2
        elif self.channelNo > 500:
            self.channelNo = 500

    def vol(self):
        volNo = int (input ("volum No: "))
        if self.onOff == 0:
            pass
        self.volNo = volNo
        if self.volNo < 2:
            self.volNo = 2
        elif self.volNo > 100:
            self.volNo = 100
    
def main(): 
    tv_name = input("What do you want to name your TV? ") 
    tv = tvSim(tv_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        TV Simulator

        0 - Quit
        1 - Turn On/Off TV
        2 - Enter a channel number
        3 - Enter a volume
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # TV On/Off
        elif choice == "1":
            tv.onOffTV()
            tv.status()

        # TV channel no
        elif choice == "2":
            tv.channel()
            tv.status()

        # raise/Low Vol
        elif choice == "3":
            tv.vol()
            tv.status()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main() 
print("\n\nPress the enter key to exit.")