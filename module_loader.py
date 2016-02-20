from error import *
import platform
import os

PLUGIN_FOLDER = 'Module'

def filer(name):
    if name[0]=='_' and name[1]=='_':
        return False
    else:
        return True

MAIN_CLASS = 'Action'

plugins = []
plugin_jar = None

for path in os.listdir(PLUGIN_FOLDER):
    if filer(path.split(os.sep)[-1]):
        if not path[-3:]=='pyc':
            plugins.append('.'.join(path.split('.')[:-1]))
            plugin_jar = __import__(PLUGIN_FOLDER+'.'+'.'.join(path.split('.')[:-1]))
