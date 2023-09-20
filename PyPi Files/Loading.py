import time
import threading as t
import shutil
from PyEnhance import Counter

Counter = Counter.Counter

Rotate = ['|', '/', '-', '\\', '|', '/', '-', '\\']


class Loading:

    def __init__(self):
        self.StopFlag = False
        self.thread = None

    def Stop(self):

        if self.thread.is_alive():
            self.StopFlag = True
            self.thread.join()

    def SpinStart(self, Text, TextBack):
        for i in Rotate:
            print(f'{Text} {i}', end="", flush=True)
            time.sleep(0.4)
            print(f'{TextBack}', end="", flush=True)

    def Spin(self, Text):
        Text = Text
        textlen = len(Text)
        TextBack = '\b' * (textlen + 2)
        if self.thread is None or not self.SpinStart:
            self.thread = t.Thread(target=self.SpinStart, args=(Text, TextBack))
            self.thread.start()

    def BarStart(self):

        columns = shutil.get_terminal_size()

        Width = columns

        Width = Width.columns

        Range = Width



        try:
            BufferBackSpace = '\b' * (Width)
            print(f"{BufferBackSpace}", end="")

            Text = 'Loading'

            Buffer = ' ' * 4

            SidesWidth = (Width - len(Text) + len(Buffer))


            for x in range(int(SidesWidth/2)):
                print(f'|', end="", flush=True)
                time.sleep(0.1)

            print(f"{Buffer}{Text}{Buffer}", end="", flush=True)

            for x in range(int(SidesWidth / 2)):
                print(f'|', end="", flush=True)
                time.sleep(0.1)

            #print(f"{BufferBackSpace}", end="")



        finally:
            Text = 'Loading'

            Buffer = ' ' * 4

            SidesWidth = (Width - len(Text) + len(Buffer))

            NewRange = SidesWidth + Width

            for i in range(int(NewRange)):

                print('\b', end="", flush=True)
                time.sleep(0.1)

    def Bar(self):
        if self.thread is None or not self.BarStart:
            self.thread = t.Thread(target=self.BarStart)
            self.thread.start()

    def StatsStart(self, List):

            ListLen = len(List)
            for i in range(ListLen+1):
                CounterVal = Counter.Counter.Count
                Counter.Counter.Add()
                ListLen = len(List)
                Progress = CounterVal / ListLen * 100
                Progress = str(Progress)


                if CounterVal == ListLen:
                    OutputString = f"Progress: {CounterVal}/{ListLen}({Progress[:5]}%)"
                    TextBack = '\b' * len(OutputString)
                    print(f"{TextBack}{OutputString}", end="", flush=True)

                else:

                    OutputString = f"Progress: {CounterVal}/{ListLen}({Progress[:4]}%)"
                    TextBack = '\b' * len(OutputString)
                    print(f"{TextBack}{OutputString}", end="", flush=True)


    def Stats(self, List):

        if self.thread is None or not self.StatsStart:
            self.thread = t.Thread(target=self.StatsStart, args=(List,))
            self.thread.start()


Loading = Loading()

Loading.Bar()
