# Copyright 2015 Alex Woroschilow (alex.woroschilow@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import sys, os
import glob
import os.path
# sys.path.append(os.path.abspath(__file__))

from pm.switcher.Usb import Usb
from pm.switcher.Usb import UsbDevice


class TouchScreen(Usb):
    def __init__(self):
        self._whitelist = ["touchscreen"]

    @property
    def name(self):
        return self.__class__.__name__.lower()

    @property
    def devices(self):
        for path_device in glob.glob("/sys/bus/usb/devices/*"):
            if os.path.isdir(path_device):
                device = UsbDevice(path_device)
                if os.path.isfile(device.product):
                    if device.name in self._whitelist:
                        yield device
        pass

    def __str__(self):
        return "Touch Screen"


if __name__ == "__main__":
    print((TouchScreen()))
    print((TouchScreen()).is_powersave)
    print([str(device) for device in (TouchScreen()).devices])
    print([str(device) for device in (TouchScreen()).powersave()])
    print([str(device) for device in (TouchScreen()).perfomance()])