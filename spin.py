#coding:utf-8
import threading
import sys
import time
import threading
import atexit

intervals = {}
_interval_ctr = 0

def _new_interval_id():
    global _interval_ctr
    _interval_ctr += 1
    return _interval_ctr

def set_interval(f,delay, *args, **kwargs):
    i_id = _new_interval_id()
    def f_major():
        f(*args, **kwargs)
        t = threading.Timer(delay,f_major)
        intervals[i_id] = t
        t.daemon = True
        t.start()
    t = threading.Timer(delay,f_major)
    intervals[i_id] = t
    t.daemon = True
    t.start()
    return i_id

def clear_interval(i_id):
    try:
        intervals[i_id].cancel()
        del intervals[i_id]
        return 0
    except KeyError:
        return 1

SPINNERS = {
    'Box1': '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏',
    'Box2': '⠋⠙⠚⠞⠖⠦⠴⠲⠳⠓',
    'Box3': '⠄⠆⠇⠋⠙⠸⠰⠠⠰⠸⠙⠋⠇⠆',
    'Box4': '⠋⠙⠚⠒⠂⠂⠒⠲⠴⠦⠖⠒⠐⠐⠒⠓⠋',
    'Box5': '⠁⠉⠙⠚⠒⠂⠂⠒⠲⠴⠤⠄⠄⠤⠴⠲⠒⠂⠂⠒⠚⠙⠉⠁',
    'Box6': '⠈⠉⠋⠓⠒⠐⠐⠒⠖⠦⠤⠠⠠⠤⠦⠖⠒⠐⠐⠒⠓⠋⠉⠈',
    'Box7': '⠁⠁⠉⠙⠚⠒⠂⠂⠒⠲⠴⠤⠄⠄⠤⠠⠠⠤⠦⠖⠒⠐⠐⠒⠓⠋⠉⠈⠈',
    'Spin1': '|/-\\',
    'Spin2': '◴◷◶◵',
    'Spin3': '◰◳◲◱',
    'Spin4': '◐◓◑◒',
    'Spin5': '▉▊▋▌▍▎▏▎▍▌▋▊▉',
    'Spin6': '▌▄▐▀',
    'Spin7': '╫╪',
    'Spin8': '■□▪▫',
    'Spin9': '←↑→↓'
}

class Spin:
    pos = 0
    words = ''
    type_ = 'Spin1'
    flag_exit = False
    
    def __init__(self,type_='Spin1',words=''):
        if words!='':
            self.words = words+' '
        else:
            pass
        self.type_=type_

    def loop_main(self):
        sys.stdout.write('\r' + self.words + self.spinner[self.pos])
        if self.pos == len(self.spinner)-1:
            self.pos = 0
        else:
            self.pos+=1

    def start(self):
        self.spinner = SPINNERS[self.type_]
        self.loop_id = set_interval(self.loop_main,0.1)

    def stop(self):
        clear_interval(self.loop_id)