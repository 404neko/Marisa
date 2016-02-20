#coding: UTF-8
import requests
import os
import re

class Action:
    
    def __init__(self,text,env):
        self.env = env
        self.text = text

    def run(self):
        array = self.text.split('/')
        array[3] = 'large'
        print 222
        url = '/'.join(array)
        respon = requests.get(url)
        f = open('Packs'+os.sep+array[-1],'wb')
        f.write(respon.content)
        f.close()
        print 222
        os.system('echo '+url+' | clip')
        return {'value':url,'notice':['t.cn','Link coverted and picture has been downloaded.'],}

    @staticmethod
    def test(text):
        import re#http://ww4.sinaimg.cn/bmiddle/8245bf01jw1f13pjyynmvj20j6eu94qq.jpg
        return len(re.findall('(http://ww[0-9]\.sinaimg\.cn/.*?(jpg|png|gif))',text))>0