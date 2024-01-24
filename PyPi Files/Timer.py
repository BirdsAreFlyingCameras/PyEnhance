import time
import threading

def TimeFormat(Counter=None, Form=None):

    Counter = Counter[0] / 60
    Counter = str(Counter)
    DotIndex = Counter.index('.')

    OutputMin = f"{Counter[:DotIndex]}"
    OutputSec = f"{Counter[DotIndex:]}"

    if DotIndex == 1 and not (round(float(OutputSec) * 60)) > 60 and int(OutputMin) == 0:  # Checks if output seconds in total are less then a min

        if OutputSec == ".":
            OutputSec = "0"
        else:
            OutputSec = (round(float(OutputSec) * 60))

        if Form == "Long":
            print(f'{OutputSec} seconds')
        else:
            if len(str(OutputSec)) == 1:
                OutputSec = f"0{OutputSec}"  # Adds a zero as the first digit if there is no first digit
            print(f'00:{OutputSec}')


    if DotIndex == 2 or int(OutputMin) > 0 and DotIndex == 1:
        if OutputSec == ".":
            OutputSec = "0"
        else:
            OutputSec = (round(float(OutputSec) * 60))

        OutputMin = ((int(OutputMin) + (int(OutputSec / 60))))

        if int(OutputMin) < 60:  # Checks if output min is less then an hour


            if Form == "Long":
                if OutputMin != 0 and OutputSec == 0:
                    print(f'{OutputMin} minutes')
                elif OutputMin == 0 and OutputSec != 0:
                    print(f'{OutputSec} seconds')
                else:
                    print(f'{OutputMin} minutes {OutputSec} seconds')
            else:
                if len(str(OutputSec)) == 1: OutputSec = f"0{OutputSec}"
                if len(str(OutputMin)) == 1: OutputMin = f"0{OutputMin}"
                print(f'{OutputMin}:{OutputSec}')

        else:
            OutputHours = (int(OutputMin / 60))
            OutputMin = (OutputMin - (int(OutputMin / 60) * 60))


            if Form == "Long":
                if OutputMin == 0 and OutputSec == 0:
                    print(f'{OutputHours} hours')
                elif OutputMin != 0 and OutputSec == 0:
                    print(f'{OutputHours} hours {OutputMin} minutes')
                elif OutputMin == 0 and OutputSec != 0:
                    print(f'{OutputHours} hours {OutputSec} Seconds')
                else:
                    print(f'{OutputHours} hours {OutputMin} minutes {OutputSec} seconds')

            else:
                if len(str(OutputSec)) == 1: OutputSec = f"0{OutputSec}"
                if len(str(OutputMin)) == 1: OutputMin = f"0{OutputMin}"
                if len(str(OutputHours)) == 1: OutputHours = f"0{OutputHours}"
                print(f'{OutputHours}:{OutputMin}:{OutputSec}')

    if DotIndex == 3 or DotIndex == 4:

        if OutputSec == ".":
            OutputSec = "0"

        OutputMin = int(OutputMin)
        OutputSec = float(OutputSec)

        OutputMin = ((OutputMin + (int(OutputSec / 60))))
        OutputSec = (round(float(OutputSec) * 60))

        if OutputMin >= 60:
            OutputMin = int(OutputMin)
            OutputHours = (int(OutputMin / 60))
            OutputMin = (OutputMin - (int(OutputMin / 60) * 60))


            if Form == "Long":
                if OutputMin == 0 and OutputSec == 0:
                    print(f'{OutputHours} hours')
                elif OutputMin != 0 and OutputSec == 0:
                    print(f'{OutputHours} hours {OutputMin} minutes')
                elif OutputMin == 0 and OutputSec != 0:
                    print(f'{OutputHours} hours{OutputSec} Seconds')
                else:
                    print(f'{OutputHours} hours {OutputMin} minutes {OutputSec} seconds')
            else:
                if len(str(OutputSec)) == 1: OutputSec = f"0{OutputSec}"
                if len(str(OutputMin)) == 1: OutputMin = f"0{OutputMin}"
                if len(str(OutputHours)) == 1: OutputHours = f"0{OutputHours}"
                print(f'{OutputHours}:{OutputMin}:{OutputSec}')


class Timer:
    def __init__(self):
        self.stop_flag = True
        self.thread = None
        self.counter = 0
        self.Stamps = None

        self.Form = None

    def counterlist(self):
        return self.counterlist

    def _run(self):

        while not self.stop_flag:
            time.sleep(1)
            self.counter += 1

    def Start(self, Form=None):

        self.Form = Form

        if self.thread is None or not self.Start:
            self.stop_flag = False
            self.thread = threading.Thread(target=self._run)
            self.thread.start()

        else:
            print(f"[ERROR] Timer already running")

    def Stop(self):
        if self.thread and self.thread.is_alive():
            self.stop_flag = True
            self.thread.join()

            self.counterlist = []

            if self.stop_flag is True:
                self.counterlist.append(self.counter)

                TimeFormat(self.counterlist, Form=self.Form)
        else:
            print(f"[ERROR] Timer not running")


Timer = Timer()

"""

=== Examples ===

Short form output:

Timer.Start()

time.sleep(30)

Timer.Stop()


Long form output:

Timer.Start(Form="Long")

time.sleep(30)

Timer.Stop()

"""
"""

TestCases = [
    3661,  # Slightly more than an hour
    45,  # Less than a minute
    7322,  # A bit more than two hours
    86399,  # One second less than a full day
    0,  # No time
    12345,  # Random intermediate value
    5400,  # Exactly one and a half hour
    3599,  # One second less than an hour
    86400,  # Exactly one day
    18000  # Exactly five hours
]

Timer.Start(TestInt=18000)

time.sleep(1)

Timer.Stop()

"""

####
"""
Left off with the issue of stamps not working 

"""
####