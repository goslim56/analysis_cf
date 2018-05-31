from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

request = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
resp = urlopen(request)
html = resp.read().decode('cp949')

bs = BeautifulSoup(html, 'html.parser')
# print(bs.prettify())

tags = bs.findAll('div', attrs={'class': 'tit3'})
# print(tag)

for index, tag in enumerate(tags):
    print(index, tag.a.text, tag.a['href'], sep=':')


