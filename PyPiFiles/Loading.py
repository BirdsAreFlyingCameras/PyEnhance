import time
import threading as t
import shutil
from PyEnhance import Counter
import sys
from prettycli import color
import cursor

cursor.hide()

Counter = Counter.Counter


class Loading:

    def __init__(self):
        self.StopFlag = False
        self.thread = None
        self.CounterObject = Counter()

        self.StyleRetro = [(97,187,70), (253,184,39), (245,130,31), (224,58,62)]

    def Stop(self):
        if self.thread.is_alive():
            self.StopFlag = True
            self.thread.join()



    def SpinStart(self, Text:str, TextBack, Ascii:bool=False, Style:str=None):

        self.AsciiRotate = ['|', '/', '-', '\\', '|', '/', '-', '\\']
        self.UniRotate = ['│', '╱', '─', '╲', '│', '╱', '─', '╲']

        while self.StopFlag is False:

            if Style == "Retro":

                if Ascii == False:
                    for Char, Color in zip(self.UniRotate, self.StyleRetro):
                        if self.StopFlag: break

                        Char = color(Char).rgb_fg(*Color)
                        print(f'{Text} {Char}', end="", flush=True)
                        time.sleep(0.4)
                        print(f'{TextBack}', end="", flush=True)
                else:
                    for Char, Color in zip(self.AsciiRotate, self.StyleRetro):
                        if self.StopFlag: break
                        Char = color(Char).rgb_fg(*Color)
                        print(f'{Text} {Char}', end="", flush=True)
                        time.sleep(0.4)
                        print(f'{TextBack}', end="", flush=True)
            else:
                if Ascii == False:
                    for i in self.UniRotate:
                        if self.StopFlag: break
                        print(f'{Text} {i}', end="", flush=True)
                        time.sleep(0.4)
                        print(f'{TextBack}', end="", flush=True)
                else:
                    for i in self.AsciiRotate:
                        if self.StopFlag: break
                        print(f'{Text} {i}', end="", flush=True)
                        time.sleep(0.4)
                        print(f'{TextBack}', end="", flush=True)

    def Spin(self, Text:str, Ascii:bool=False, Style:str=None):
        textlen = len(Text)
        TextBack = '\b' * (textlen + 2)
        if self.thread is None or not self.SpinStart:
            self.thread = t.Thread(target=self.SpinStart, args=(Text, TextBack, Ascii, Style))
            self.thread.start()



    def BarStart(self, PrintSpeed:int, Ascii:bool=False):

        columns = shutil.get_terminal_size()

        Width = columns

        Width = Width.columns

        while self.StopFlag is False:

            if self.StopFlag:
                break

            BufferBackSpace = '\b' * Width
            print(f"{BufferBackSpace}", end="")
            Text = 'Loading'
            Buffer = ' ' * 4
            SidesWidth = (Width - len(Text) - len(Buffer * 2))

            for _ in range(int(SidesWidth / 2)):

                if self.StopFlag:
                    break
                if Ascii == False:
                    print('▍', end="", flush=True)
                    time.sleep(PrintSpeed)
                else:
                    print('|', end="", flush=True)
                    time.sleep(PrintSpeed)

            for i in Buffer:

                if self.StopFlag:
                    break

                print(f'{i}', end="", flush=True)
                time.sleep(PrintSpeed)

            for i in Text:

                if self.StopFlag:
                    break

                print(f"{i}", end="", flush=True)
                time.sleep(PrintSpeed)

            for i in Buffer:
                if self.StopFlag:
                    break

                print(f'{i}', end="", flush=True)
                time.sleep(PrintSpeed)

            for _ in range(int(SidesWidth / 2)):

                if self.StopFlag:
                    break

                if Ascii == False:
                    print('▍', end="", flush=True)
                    time.sleep(PrintSpeed)
                else:
                    print('|', end="", flush=True)
                    time.sleep(PrintSpeed)

            Buffer = ' ' * 4

            NewRange = Width + len(Buffer * 2)

            for i in range(int(NewRange)):

                if self.StopFlag:
                    break

                sys.stdout.write('\b \b')
                sys.stdout.flush()
                time.sleep(PrintSpeed)

    def Bar(self, PrintSpeed:int, Ascii:bool=False):

        if self.thread is None or not self.BarStart:
            self.thread = t.Thread(target=self.BarStart, args=(PrintSpeed, Ascii))
            self.thread.start()



    def StatsStart(self, Range:int, Counter):

        CounterVal = Counter.Total

        Progress = CounterVal / Range * 100

        Progress = str(Progress)

        if CounterVal == Range:
            OutputString = f"Progress: {CounterVal}/{Range}({Progress[:5]}%)"
            TextBack = '\b' * len(OutputString)
            print(f"{TextBack}{OutputString}", end="", flush=True)


        else:
            OutputString = f"Progress: {CounterVal}/{Range}({Progress[:4]}%)"
            TextBack = '\b' * len(OutputString)
            print(f"{TextBack}{OutputString}", end="", flush=True)

    def Stats(self, Range:int):
        self.CounterObject.Add()
        if self.thread is None or not self.thread.is_alive():
            self.thread = t.Thread(target=self.StatsStart, args=(Range, self.CounterObject,))
            self.thread.start()


    def BounceStart(self, Text:str, Speed:int or float):

        Text = Text.lower()

        Textlist = list(Text.lower())

        while self.StopFlag is False:

            for Char in Textlist:

                if self.StopFlag:
                    break

                TextBack = '\b' * len(Text)
                BounceCharIndex = Text.index(Char)

                Textlist[BounceCharIndex] = str(Textlist[BounceCharIndex]).upper()

                String = ''.join(Textlist)

                print(f"{TextBack}{String}", end="", flush=True)

                time.sleep(Speed)

                Textlist[BounceCharIndex] = str(Textlist[BounceCharIndex]).lower()

    def Bounce(self, Text:str, Speed:int or float):
        if self.thread is None or not self.thread.is_alive():
            self.thread = t.Thread(target=self.BounceStart, args=(Text, Speed,))
            self.thread.start()


"""

===EXAMPLES===

Stats:

ExampleList = [1, 2, 3, 4, 5]

for i in range(len(ExampleList)):
    time.sleep(0.5)

    Loading.Stats(Range=len(ExampleList))


Bar:

	print("\n"*5)

	Loading.Bar(PrintSpeed=0.1)

	time.sleep(60)

	Loading.Stop()


Spin:

	Loading.Spin(Text="Loading")
	time.sleep(30)
	Loading.Stop()

"""
