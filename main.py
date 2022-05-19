import selenium
import requests
from bs4 import BeautifulSoup as bs

def replace_esc(text):
    esc = ["\t","\n"]
    for i in esc:
        text = text.replace(i,"")
    return text
with requests.Session() as s:
    noticePage = s.get("https://lostark.game.onstove.com/News/Notice/List")
    soup = bs(noticePage.text,"html.parser")
    contents = soup.find_all("ul")[11]
    title = contents.find_all("a")
    label = []
    for i in title:
        i.find_all("div")
        seg = []
        for q in i:
            rebuild = replace_esc(q.text)
            if rebuild != "":
                seg.append(rebuild)
        label.append(seg)
    res = []
    for i in label:
        res.append([i[0],i[1],i[3]])
    for i in res:
        print(i)