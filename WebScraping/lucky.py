#! python3
# lucky.py - Opens several Google search results.

import requests,sys,bs4,webbrowser

print('Googling...')# display text while downloading the Google page
# res=requests.get('http://baidu.com/s?wd='+' '.join(sys.argv[1:]))
res=requests.get('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=google&oq=google&rsv_pq=88ca6fe8000103c7&rsv_t=e489I6DZkgJhQMQ5%2Fy%2BqN2K3hW4fNmi87bxAuK3y538Nq9PbuU5aYjU4%2Br4&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_sug3=1&rsv_sug4=936&bs=google&rsv_jmp=fail')
res.raise_for_status()



# TODO: Retrieve top search result links.
soup=bs4.BeautifulSoup(res.text)
# TODO: Open a brower tab for each result.
linkElems=soup.select('.t a')
numOpen=min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com'+linkElems[i].get('href'))