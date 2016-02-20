from main_module_loader import *
import AsyncIO
import spin

CONFIG = {
    'module':'default',
    'HIDE':1
}

from config import *


clipboard_ = clipboard.ClipBoard()
#interface_ = interface.Interface()

import time

AsyncIO.init()

    

last = clipboard_.get()

spin_ = spin.Spin()
spin_.start()
while True:
    
    time.sleep(0.5)
    clipboard_data = clipboard_.get()
    if clipboard_data[0] in ['UNICODE','TEXT']:
        text = clipboard_data[1]
        if text==last:
            continue
        else:
            print text
            AsyncIO.PutOne_Direct(text)
            last = text