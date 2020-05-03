#!/usr/bin/env python3
"""
@author: Vadim
"""
from subprocess import Popen, PIPE
import time
import pyautogui
from collections import namedtuple

Rect = namedtuple("Rect", "left top right bottom")


class ControlledApp:
    caption: str  # aaplication name to find
    path: str  # path for application to start
    startup_time: int  # application startup time in seconds
    app_win: object  # app window

    def __init__(self, path: str, caption: str, startup_time: int):
        """
        :param path: file path for application to start
        :param caption: application name to find among processes. Used if start_new = False
        :param startup_time: application startup time in seconds
        """
        self.path = path
        self.caption = caption
        self.startup_time = startup_time
        pass

    def start(self):
        pass

    def init_app(self, start_new: bool):
        """If start_new = False than try to use opened app, other case - create new. Brings to front the Window
        :param start_new: True = always create new process
        """

        if start_new:
            Popen([self.path], stdout=PIPE, universal_newlines=True)
            time.sleep(self.startup_time)
        winWA = pyautogui.getWindowsWithTitle(self.caption)
        for curr_win in winWA:
            if curr_win.left>0 and curr_win.right>0 and curr_win.top>0 and curr_win.bottom>0:
                self.app_win = curr_win
                break
        self.app_win.activate()
        pass
    def test_Nastya_say_hello(self):
        # Activate Whatsapp window
        winWA = pyautogui.getWindowsWithTitle(self.caption)
        for curr_win in winWA:
            if curr_win.left>0 and curr_win.right>0 and curr_win.top>0 and curr_win.bottom>0:
                self.app_win = curr_win
                break
        self.app_win.activate()
        # Click to Search field
        whatsapp_field_to = Rect(left=96, top=128, right=391, bottom=153)
        pyautogui.click(x=self.app_win.left + (whatsapp_field_to.left + whatsapp_field_to.left)/2,
                        y=self.app_win.top + (whatsapp_field_to.top + whatsapp_field_to.bottom)/2)
        time.sleep(1)
        # Type "Настя"
        pyautogui.hotkey('alt', 'shift')
        time.sleep(1)
        pyautogui.write('Yfcnz', interval=0.25)
        # Choose first from the list
        whatsapp_list_first = Rect(left=15, top=273, right=356, bottom=334)
        pyautogui.click(x=self.app_win.left + (whatsapp_list_first.left + whatsapp_list_first.left)/2,
                        y=self.app_win.top + (whatsapp_list_first.top + whatsapp_list_first.bottom)/2)
        time.sleep(1)
        # Write hello
        text_msg_box = Rect(left=387, top=52, right=110, bottom=27)  # min_dimentions from bottom
        pyautogui.click(x=self.app_win.right - (text_msg_box.left + text_msg_box.left)/2,
                        y=self.app_win.bottom - (text_msg_box.top + text_msg_box.bottom)/2)
        pyautogui.write('Ghbdtn nt,t ptvkzyby jn fdnj,jnjd!', interval=0.1)
        pyautogui.press('enter')
        pass
