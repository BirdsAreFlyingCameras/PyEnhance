import time
import threading
from Stamps import *

def TimeFormat(Counter=None, Stamps=bool):

    print(f"Int being Testing: {Counter[0]}")

    CounterToString = Counter[0]
    CounterToString = str(CounterToString)

    Counter = Counter[0] / 60
    Counter = str(Counter)
    #Counter = Counter[:5]
    DotIndex = Counter.index('.')

    #print(f"Counter: {Counter}")
    #print(f"Dot Index: {DotIndex}")

    OutputMin = f"{Counter[:DotIndex]}"
    OutputSec = f"{Counter[DotIndex:]}"

    #print(f"Output Min: {OutputMin}")
    #print(f"Output Sec: {OutputSec}")
    #print(f"Output Sec Float Rounded: {(round(float(OutputSec) * 60))}")

    if DotIndex == 1 and not (round(float(OutputSec) * 60)) > 60 and int(OutputMin) == 0: # Checks if output seconds in total are less then a min
        #print("Flag")

        if OutputSec == ".":
            OutputSec = "0"
        else:
            OutputSec = (round(float(OutputSec) * 60))

        if len(str(OutputSec)) == 1:
            OutputSec = f"0{OutputSec}"

        print(f'00:{OutputSec}')


    if DotIndex == 2 or int(OutputMin) > 0 and DotIndex == 1:
        if OutputSec == ".":
            OutputSec = "0"
        else:
            OutputSec = (round(float(OutputSec) * 60))

        OutputMin = ((int(OutputMin) + (int(OutputSec / 60))))



        if len(str(OutputSec)) == 1:
            OutputSec = f"0{OutputSec}"
        if len(str(OutputMin)) == 1:
            OutputMin = f"0{OutputMin}"



        if int(OutputMin) < 60: # Checks if output min is less then an hour
            print(f"Out Sec: {OutputSec}")

            if Stamps == True:
                print(f"{Stamp.Output} Time Elapsed: {OutputMin}:{OutputSec}")
            else:
                print(f"Time Elapsed: {OutputMin}:{OutputSec}")

        else:
            OutputHours = (int(OutputMin / 60))
            OutputMin = (OutputMin - (int(OutputMin / 60) * 60))

            if len(str(OutputSec)) == 1:
                OutputSec = f"0{OutputSec}"
            if len(str(OutputMin)) == 1:
                OutputMin = f"0{OutputMin}"

            if Stamps == True:
                print(f"{Stamp.Output} {Stamp.Output} {OutputHours}:{OutputMin}:{OutputSec}")
            else:
                print(f"{OutputHours}:{OutputMin}:{OutputSec}")



    if DotIndex == 3 or DotIndex == 4:

        #print("DotIndex: 3")

        #print(f"min: {OutputMin}")
        #print(f"Sec: {OutputSec}")

        if OutputSec == ".":
            OutputSec = "0"

        OutputMin = int(OutputMin)
        OutputSec = float(OutputSec)



        #print(f"min: {OutputMin}")
        #print(f"Sec: {OutputSec}")

        OutputMin = ((OutputMin + (int(OutputSec / 60))))
        OutputSec = (round(float(OutputSec) * 60))


        if OutputMin >= 60:
            print("Over 60")
            OutputMin = int(OutputMin)
            OutputHours = (int(OutputMin / 60))
            OutputMin = (OutputMin - (int(OutputMin / 60) * 60))

            if len(str(OutputSec)) == 1:
                OutputSec = f"0{OutputSec}"
            if len(str(OutputMin)) == 1:
                OutputMin = f"0{OutputMin}"

            if Stamps == True:
                print(f"{Stamp.Output} Time Elapsed: {OutputHours}:{OutputMin}:{OutputSec}")
                print(f"{Stamp.Output} Time Elapsed: {OutputHours} Hours {OutputMin} Minutes {OutputSec} Seconds")
            else:
                print(f"Time Elapsed: {OutputHours}:{OutputMin}:{OutputSec}")
                print(f"Time Elapsed: {OutputHours} Hours {OutputMin} Minutes {OutputSec} Seconds")


class Timer:
    def __init__(self):
        self.stop_flag = True
        self.thread = None
        self.counter = 0
        self.Stamps = None

        self.TestInt = None # REMOVE JUST FOR TESTING

    def counterlist(self):
        return self.counterlist

    def _run(self):

        while not self.stop_flag:
            time.sleep(1)
            self.counter += 1

    def Start(self, Stamps=bool, TestInt=None): # REMOVE TEST INT

        self.TestInt = TestInt

        self.Stamps = Stamps


        if self.thread is None or not self.Start:
            self.stop_flag = False
            self.thread = threading.Thread(target=self._run)
            self.thread.start()
            if Stamps == True:
                print(f"{Stamp.Info} Timer Started")
        else:

            if Stamps == True:
                print(f"{Stamp.Error} Timer already running")
            else:
                print(f"Timer already running")

    def Stop(self):
        if self.thread and self.thread.is_alive():
            self.stop_flag = True
            self.thread.join()
            if self.Stamps == True:
                print(f"{Stamp.Info} Timer Stopped")

            global Counter


            self.counter = self.TestInt # CHANGED FOR TESTING CHANGE BACK DLEATE ME WHEN DONE
            Counter = self.counter



            self.counterlist = []

            if self.stop_flag is True:

                self.counterlist.append(self.counter)
                Counter = self.counterlist

                TimeFormat(Counter)

        else:
            if self.Stamps == True:
                print(f"{Stamp.Error} Timer not running")
            else:
                print(f"Timer not running")

Timer = Timer()


"""

=== Examples ===

Timer.Start(Stamps=True)

time.sleep(30)

Timer.Stop()

"""
TestCases = [
    3661,    # Slightly more than an hour
    45,      # Less than a minute
    7322,    # A bit more than two hours
    86399,   # One second less than a full day
    0,       # No time
    12345,   # Random intermediate value
    5400,    # Exactly one and a half hour
    3599,    # One second less than an hour
    86400,   # Exactly one day
    18000    # Exactly five hours
]



Timer.Start(Stamps=False,TestInt=18000)

time.sleep(1)

Timer.Stop()

