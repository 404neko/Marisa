#coding: UTF-8

class Action:
    
    def __init__(self,text,env):
        self.env = env
        self.text = text

    def run():
        #do something
        return {'value':'','notice':['',''],}

    @staticmethod
    def test(text):
        import re
        return len(re.findall('http://m\.coolapk\.com/(game|apk)/.*',text))>0