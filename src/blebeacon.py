#!/usr/bin/python
import re

class blebeacon(object):
    """docstring for blebeacon"""
    def __init__(self, RSS, SSID, BSS):
        super(blebeacon, self).__init__()
        self.BSS = BSS
        self.RSS = self.num(RSS)
        self.SSID = SSID


    def num(self, s):
        try:
            return int(s)
        except ValueError:
            return float(s)

def main(arg):
    pass

if __name__ == "__main__":
    main()
