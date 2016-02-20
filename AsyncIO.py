#-*- coding:utf-8 -*-

import threading
from Queue import Queue
import os
import time
import sys
import re
import requests
import interface.Windows

from module_loader import *

module_obj = []

for plugin in plugins:
    module_obj.append(getattr(plugin_jar,plugin))


interface_ = interface.Windows.Interface()



def Log(String):
    print time.strftime('%I:%M:%S',time.localtime(time.time()))+' - '+String



def Download(String):
    for plugin in module_obj:
        #print dir(plugin)
        if plugin.Action.test(String):
            object_ = plugin.Action(String,env=None)
            respon = object_.run()
            notice = respon.get('notice',False)
            if notice:
                interface_.ShowBalloon(notice[0],notice[1])
            else:
                pass
            return respon['value']
        else:
            pass

class AsyncIODirect(threading.Thread):
    ToWrite=Queue()

    def __init__(self):
        threading.Thread.__init__(self)
        self.name='AsyncIODirect'

    def run(self):
        while True:
            Data=AsyncIODirect.ToWrite.get()
            Download(Data)

def PutOne_Direct(Data):
    AsyncIODirect.ToWrite.put(Data)

def init():
    
    App=AsyncIODirect()
    App.setDaemon(True)
    App.start()