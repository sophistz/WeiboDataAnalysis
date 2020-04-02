import requests
import json
import queue

url = 'https://m.weibo.cn/api/statuses/repostTimeline'
url = "https://www.baidu.com"
data = {
	'id':'4467068826659732',
	'page':1
}


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
}

response = requests.get(url, params=data, headers=headers)
response = requests.get(url, headers=headers)
# response.encoding="utf-8"
text = response.text
print(text)