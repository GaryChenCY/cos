#抓取網頁原始碼
import urllib.request as req
url="https://www.ptt.cc/bbs/Gossiping/index2.html"

#建立request物件
request=req.Request(url, headers={
    "cookie":"over18=1",
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
import bs4
root=bs4.BeautifulSoup(data, "html.parser")#BeautifulSoup是專於讀取html格式
titles=root.find_all("div", class_="title")#尋找class="title"的div標籤
for title in titles:
    if title.a !=None:#如果標題包含a標籤(沒有被印出來) 印出來
        print(title.a.string)