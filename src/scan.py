#!/usr/bin/python

import time
import threading

import BLEHandler
import blebeacon
import TextParser

class ble_obs(object):
    """docstring for ble_obs"""
    def __init__(self):
        super(ble_obs, self).__init__()
        self.beacons = list()
        self.bleHandler = BLEHandler.BLEHandler()
        self.ret = self.bleHandler.scan()
        self.text_parser = TextParser.TextParser()

        print "Scanning has been done"

        self.text_parser.parse(self.ret)
        self.beaconList = self.text_parser.beaconList

        for i in range(len(self.beaconList)):
            print "BEACON ID: ", i
            print "RSS: ", self.beaconList[i].RSS
            print "BSS: ", self.beaconList[i].BSS
            print "SSID: ", self.beaconList[i].SSID


if __name__ == "__main__":
    wifi_obs = ble_obs()
