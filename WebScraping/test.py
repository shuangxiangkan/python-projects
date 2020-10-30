import requests

res=requests.get("http://www.baidu.com")
res.raise_for_status()
print(len(res.text))
print(res.text)