import requests
import json
import queue

url = 'https://m.weibo.cn/api/statuses/repostTimeline'
data = {
	'id':'4467068826659732',
	'page':1
}


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
    }

oneWeiboRepost = {}
q = queue.Queue()

def fetch():
	try:
		response = requests.get(url,params=data,headers=headers)
		jsonData = json.loads(response.text)['data']
		return jsonData
	except Exception as e:
		print(e)
		return {}

def getHtml(frt):
	ret = {}
	retInfo = []
	jsonData = fetch()
	if jsonData == {}:
		return {}
	for e in jsonData['data']:
		if e['raw_text'].find("//@")  != -1:
			continue
		retInfo.append(e['id'])
	lenRepostList = jsonData['total_number']
	lenRepostList = lenRepostList - len(jsonData['data'])
	i = 2
	while lenRepostList > 0:
		data['page'] = i
		jsonData = fetch()
		if (jsonData == {}):
			continue
		for e in jsonData['data']:
			if (e['raw_text'].find("//@")) != -1:
				continue
			retInfo.append(e['id'])
			print(e['id'])
		i = i + 1
		lenRepostList = lenRepostList - len(jsonData["data"])
	ret['id'] = frt
	ret['repost'] = retInfo
	return ret

def bfs():
	layer = 0
	allInfo = []
	while not q.empty():
		layer = layer + 1
		oneLayerInfo = {}
		l = q.qsize()
		oneLayer = []
		for i in range(0,l):
			frt = q.get()
			data['id'] = frt
			data['page'] = 1
			res = getHtml(frt)
			if (res == {}):
				continue
			for e in res['repost']:
				q.put(e)
			oneLayer.append(res)
		if oneLayer == []:
			continue
		oneLayerInfo['layer'] = layer
		oneLayerInfo['allRepostInfo'] = oneLayer
		allInfo.append(oneLayerInfo)
		
	print(allInfo)

q.put('4488637502218080')
bfs()