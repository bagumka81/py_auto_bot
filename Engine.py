#!/usr/bin/env python3
"""
@author: Vadim
"""
from ControlledApp import ControlledApp


class Engine:

    def play(self):
        self.test_whatsapp()
        pass

    def test_whatsapp(self):
        whatsApp = ControlledApp("C:/Users/user/AppData/Local/WhatsApp/WhatsApp.exe",
                                 caption="WhatsApp", startup_time=5)
        #whatsApp.init_app(start_new=True)
        whatsApp.test_Nastya_say_hello()
        pass
