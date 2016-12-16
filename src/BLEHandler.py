#!/usr/bin/python
import threading
import subprocess
import time
import os
import signal

class BLEHandler(object):
    """docstring for BLEHandler"""
    def __init__(self):
        super(BLEHandler, self).__init__()
        self.response = None
        self.result = None
        self.process = None
        self.output = None
        self.err = None

    # def scan(self):
    def scan(self):
        try:
            print "Scanning has been started"
            self.process = subprocess.check_output(["bluez-test-discovery"],shell=True, preexec_fn=os.setsid)
            # self.output, self.err = self.process.communicate()
            # os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            # subprocess.check_output()
            print "Scanning has been completed"
            # print self.process
        except Exception as e:
            print "Exception caught"
            print e
        # return self.output, self.err
        return self.process

def main():
    pass

if __name__ == "__main__":
    main()
