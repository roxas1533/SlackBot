import urllib.request
import json

import datetime

trainList = ['中央線快速電車', '多摩湖線', '総武']


class TrainInfo:
    def m(self):
        url = 'https://tetsudo.rti-giken.jp/free/delay.json'
        response = urllib.request.urlopen(url)
        content = json.loads(response.read().decode('utf8'))
        text = "～遅延情報～\n"
        flag = False
        for con in content:
            for t in trainList:
                if t in con['name']:
                    lastTime = datetime.datetime.fromtimestamp(con['lastupdate_gmt'])
                    text += con['name']+",更新時間：{0:%H:%M}\n".format(lastTime)
                    flag = True
        if not flag:
            text = ""
        return text
