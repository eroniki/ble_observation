#!/usr/bin/python

import time
import threading

import BLEHandler
import blebeacon
import TextParserBLE

from ble_observation.srv import BLEArrayService
from ble_observation.srv import BLEArrayServiceResponse
from ble_observation.msg import BLEMessage

from std_msgs.msg import Header
from std_msgs.msg import String
from std_msgs.msg import Int64

import rospy

class ble_obs(object):
    """docstring for ble_obs"""
    def __init__(self):
        super(ble_obs, self).__init__()
        rospy.init_node('wifi_obs_server')
        self.s = rospy.Service('ble_observation', BLEArrayService, self.handle_ble_obs)

        self.beacons = list()
        self.bleHandler = BLEHandler.BLEHandler()
        # self.ret = self.bleHandler.scan()
        self.text_parser = TextParserBLE.TextParserBLE()

        rospy.loginfo("Ready to send wifi observations")
        rospy.spin()

        # print "Scanning has been done"
        #
        # self.text_parser.parse(self.ret)
        # self.beaconList = self.text_parser.beaconList
        #
        # for i in range(len(self.beaconList)):
        #     print "BEACON ID: ", i
        #     print "RSS: ", self.beaconList[i].RSS
        #     print "BSS: ", self.beaconList[i].BSS
        #     print "SSID: ", self.beaconList[i].SSID

    def construct_response(self):
        response = BLEArrayServiceResponse()
        obsList = list()
        for i in range(len(self.beacons)):
            obs = BLEMessage()
            obs.ssid = self.beacons[i].SSID
            obs.mac = self.beacons[i].BSS
            obs.rss = self.beacons[i].RSS
            obsList.append(obs)

        if(len(self.beacons)>0):
            response.success = True
            response.message = "Success!"
            response.observations = obsList
        else:
            response.success = False
            response.message = "Error!"

            return response

    def handle_ble_obs(self, data):
        rospy.loginfo("Service request captured")
        self.reading =  self.bleHandler.query()
        self.text_parser.parse(self.reading)
        self.beacons = self.text_parser.beaconList
        return self.construct_response()


if __name__ == "__main__":
    wifi_obs = ble_obs()
