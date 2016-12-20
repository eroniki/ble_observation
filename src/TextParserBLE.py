#!/usr/bin/python
import re
import blebeacon

class TextParserBLE(object):
    """docstring for TextParserBLE"""
    def __init__(self):
        super(TextParserBLE, self).__init__()
        self.__BSSList    = None
        self.__RSSList    = None
        self.__SSIDList   = None
        self.__zippedList = None
        self.__RSS        = None
        self.__BSS        = None
        self.__ap         = None
        self.beaconList   = list()

    def parse(self, iw_dump):
        self.__BSSList  = None
        self.__RSSList  = None
        self.__SSIDList = None
        self.__reading  = iw_dump
        self.beaconList = list()
        self.findBSS(r"\[.*\]\n")
        self.findRSS(r"RSSI.*\n")
        self.findSSID(r"Alias.*\n")
        self.createbeaconList()


    def findBSS(self, hash):
        self.__BSSList = re.findall(hash, self.__reading)

        for i in range(len(self.__BSSList)):
            self.__BSSList[i] = self.__BSSList[i].replace("[ ", "")
            self.__BSSList[i] = self.__BSSList[i].replace(" ]\n", "")

    def findRSS(self, hash):
        self.__RSSList = re.findall(hash, self.__reading)

        for i in range(len(self.__RSSList)):
            self.__RSSList[i] = self.__RSSList[i].replace("RSSI = ", "")
            self.__RSSList[i] = self.__RSSList[i].replace("\n", "")

    def findSSID(self, hash):
        self.__SSIDList = re.findall(hash, self.__reading)

        for i in range(len(self.__SSIDList)):
            self.__SSIDList[i] = self.__SSIDList[i].replace("Alias = ", "")
            self.__SSIDList[i] = self.__SSIDList[i].replace("\n", "")


    def createbeaconList(self):
        zippedList = zip(self.__RSSList, self.__BSSList, self.__SSIDList)

        for i in zippedList:
            self._RSS = i[0]
            self._BSS = i[1]
            self._SSID = i[2]
            self._beacon = blebeacon.blebeacon(BSS=self._BSS, RSS=self._RSS, SSID=self._SSID)
            self.beaconList.append(self._beacon)

    def printbeaconList(self):
        for i in range(len(self.beaconList)):
            print self.beaconList[i].SSID, self.beaconList[i].BSS, self.beaconList[i].RSS

def main(arg):
    pass

if __name__ == "__main__":
    main()
