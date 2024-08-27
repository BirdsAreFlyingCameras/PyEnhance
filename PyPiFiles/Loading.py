import time
import threading as t
import shutil

import colorama
from PyEnhance import Counter
import sys
from prettycli import color
import cursor

from colorama import init, Fore, Back
from colorama import Style as colorama_style

cursor.hide()

Counter = Counter.Counter


class Loading:

    def __init__(self):
        self.StopFlag = False
        self.thread = None
        self.CounterObject = Counter() # Used In Stats Function


    def Stop(self):
        if self.thread.is_alive():
            self.StopFlag = True
            self.thread.join()



    def SpinStart(self, Text:str, TextBack, Ascii:bool=False, Style:str=None, Speed:int or float=0.4):

        Colors = {

            "RetroGreen": (97,187,70), "RetroOrange": (245,130,31),
            "RetroYellow": (253,184,39), "RetroRed": (224,58,62),
            "RetroBlue": (87, 85, 254), "RetroTeal": (34, 166, 153)


        }

        AsciiRotate = ['|', '/', '-', '\\', '|', '/', '-', '\\']
        UniRotate = ['│', '╱', '─', '╲', '│', '╱', '─', '╲']

        StyleRetro = [(97,187,70), (253,184,39), (245,130,31), (224,58,62)]

        while self.StopFlag is False:
            if Style == "Retro":
                if Ascii is False:
                    for Char, Color in zip(UniRotate, StyleRetro):
                        if self.StopFlag:
                            break

                        Char = color(Char).rgb_fg(*Color)
                        print(f'{Text} {Char}', end="", flush=True)
                        time.sleep(Speed)
                        print(f'{TextBack}', end="", flush=True)

                else:
                    for Char, Color in zip(AsciiRotate, StyleRetro):
                        if self.StopFlag: break
                        Char = color(Char).rgb_fg(*Color)
                        print(f'{Text} {Char}', end="", flush=True)
                        time.sleep(Speed)
                        print(f'{TextBack}', end="", flush=True)

            else:

                if Ascii is False:
                    for i in UniRotate:
                        if self.StopFlag: break
                        print(f'{Text} {i}', end="", flush=True)
                        time.sleep(Speed)
                        print(f'{TextBack}', end="", flush=True)

                else:
                    for i in AsciiRotate:
                        if self.StopFlag: break
                        print(f'{Text} {i}', end="", flush=True)
                        time.sleep(Speed)
                        print(f'{TextBack}', end="", flush=True)

    def Spin(self, Text:str="Loading:", Ascii:bool=False, Style:str=None, Speed:int or float=0.4):
        TextLen = len(Text)
        TextBack = '\b' * (TextLen + 2)
        if self.thread is None or not self.SpinStart:
            self.thread = t.Thread(target=self.SpinStart, args=(Text, TextBack, Ascii, Style, Speed))
            self.thread.start()



    def BarStart(self, PrintSpeed:int, Ascii:bool=False, Style:str="Connected"):

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

                if Style == "Connected":
                    print('█', end="", flush=True)
                    time.sleep(PrintSpeed)
                elif Style == "Spaced":
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

                if Style == "Connected":
                    print('█', end="", flush=True)
                    time.sleep(PrintSpeed)
                elif Style == "Spaced":
                    print('▍', end="", flush=True)
                    time.sleep(PrintSpeed)
                else:
                    print('|', end="", flush=True)
                    time.sleep(PrintSpeed)


            Buffer = ' ' * 4
            NewRange = Width + len(Buffer * 2)

            for _ in range(int(NewRange)):

                if self.StopFlag:
                    break

                sys.stdout.write('\b \b')
                sys.stdout.flush()
                time.sleep(PrintSpeed)

    def Bar(self, PrintSpeed:int or float, Ascii:bool=False, Style:str="Connected"):

        """
        :param PrintSpeed: Time inbetween new bar segments being printed
        :param Ascii: Use ascii chars to show the bar
        :param Style: Connected or Spaced : Connected: █████  or Spaced: ▍▍▍▍▍
        :return:
        """

        if self.thread is None or not self.BarStart:
            self.thread = t.Thread(target=self.BarStart, args=(PrintSpeed, Ascii, Style))
            self.thread.start()



    def StatsStart(self, Range:int, Counter, Style:str="Full"):

        CounterVal = Counter.Total

        Progress = CounterVal / Range * 100

        Progress = str(Progress)

        if Style == "Full":

            if CounterVal == Range:
                OutputString = f"Progress: {CounterVal}/{Range} ({Progress[:5]}%)"
                TextBack = '\b' * len(OutputString)
                print(f"{TextBack}{OutputString}", end="", flush=True)
            else:
                OutputString = f"Progress: {CounterVal}/{Range} ({Progress[:4]}%)"
                TextBack = '\b' * len(OutputString)
                print(f"{TextBack}{OutputString}", end="", flush=True)

        if Style =="Min":

            if CounterVal == Range:
                OutputString = f"Progress: {Progress[:5]}%"
                TextBack = '\b' * len(OutputString)
                print(f"{TextBack}{OutputString}", end="", flush=True)
            else:
                OutputString = f"Progress: {Progress[:4]}%"
                TextBack = '\b' * len(OutputString)
                print(f"{TextBack}{OutputString}", end="", flush=True)


    def Stats(self, Range:int, Style:str="Full"):
        self.CounterObject.Add()
        if self.thread is None or not self.thread.is_alive():
            self.thread = t.Thread(target=self.StatsStart, args=(Range, self.CounterObject, Style))
            self.thread.start()



    def BounceStart(self, Text:str, Speed:int or float, Style:str="Straight"):


        colorama.init()

        Text = Text.lower()

        Textlist = list(Text.lower())

        while self.StopFlag is False:

            if Style == "Center":
                while self.StopFlag is False:

                    for Char in Textlist:

                        if self.StopFlag:
                            break

                        TextBack = '\b' * len(Text)
                        BounceCharIndex1 = Text.index(Char)
                        BounceCharIndex2 = (len(Text) - Text.index(Char))-1

                        Textlist[BounceCharIndex1] = str(Textlist[BounceCharIndex1]).upper()
                        Textlist[BounceCharIndex2] = str(Textlist[BounceCharIndex2]).upper()

                        String = ''.join(Textlist)

                        print(f"{TextBack}{colorama_style.BRIGHT}{String}", end="", flush=True)

                        time.sleep(Speed)

                        Textlist[BounceCharIndex1] = str(Textlist[BounceCharIndex1]).lower()
                        Textlist[BounceCharIndex2] = str(Textlist[BounceCharIndex2]).lower()


            if Style == "Straight":
                while self.StopFlag is False:

                    for Char in Textlist:
                        if self.StopFlag:
                            break

                        TextBack = '\b' * len(Textlist)
                        BounceCharIndex1 = Textlist.index(Char)

                        Textlist[BounceCharIndex1] = str(Textlist[BounceCharIndex1]).upper()

                        String = ''.join(Textlist)

                        print(f"{TextBack}{colorama_style.BRIGHT}{String}", end="", flush=True)

                        time.sleep(Speed)


                    for Index in range(1, len(Text)):

                        TextBack = '\b' * len(Text)
                        BounceCharIndex1 = Index

                        Textlist[BounceCharIndex1] = str(Textlist[BounceCharIndex1]).lower()

                        String = ''.join(Textlist)

                        print(f"{TextBack}{colorama_style.BRIGHT}{String}", end="", flush=True)

                        time.sleep(Speed/3)





    def Bounce(self, Text:str, Speed:int or float, Style:str="Straight"):
        if self.thread is None or not self.thread.is_alive():
            self.thread = t.Thread(target=self.BounceStart, args=(Text, Speed, Style,))
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
