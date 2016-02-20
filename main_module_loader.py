from error import *
import platform

try:
    clipboard = __import__('clipboard.'+platform.system())
    clipboard = eval('clipboard.'+platform.system())
except:
    print 'FAULT - in AfterCopy.main_import.'
    raise NecessaryLibraryNotFound('clipboard')
