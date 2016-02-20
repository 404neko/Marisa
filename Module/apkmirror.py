#coding: UTF-8
import requests
import os
import re

class Action:
    
    def __init__(self,text,env):
        self.env = env
        self.text = text

    def run(self):
        string = self.text
        content = requests.get(string).content
        link = re.findall('((https|http)://www\.apkmirror\.com/wp-content/themes/APKMirror/download.php\?id=[0-9]*?)"',content)
        respon = requests.get(link)
        name = string.split('/')[-2]+'.apk'
        respon = requests.get(link[0])
        f = open('Packs'+os.sep+name,'wb')
        f.write(respon.content)
        f.close()
        return {'value':name,'notice':['ApkMirror',name],}

    @staticmethod
    def test(text):
        import re
        return len(re.findall('(https|http)://www\.apkmirror\.com/apk/.*?/.*?/.*?/',text))>0