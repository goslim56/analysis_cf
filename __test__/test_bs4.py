# beautifulsoup4 test

from bs4 import BeautifulSoup

html = '<td class="title"><div class="tit3" id="title-test">' \
       '<a href="/movie/bi/mi/basic.nhn?code=158178" title="독전">독전</a></div></td>'

# 1. 조회
def ex1():
       bs = BeautifulSoup(html, 'html.parser')
       print(bs, type(bs))

       tag = bs.td
       print(tag, type(tag))
       print(tag.div)

       tag = bs.a
       print(tag, type(tag))
       print(tag.name)



# 2. Attribute 값
def ex2():
       bs = BeautifulSoup(html, 'html.parser')

       tag = bs.td
       print(tag['class'])

       tag = bs.div
       print(tag['id'])
       print(tag.attrs)

# 3. Attribute 조회
def ex3():
       bs = BeautifulSoup(html, 'html.parser')

       tag = bs.find('td', attrs={'class': 'title'})
       print(tag)
       
       tag = bs.find(attrs={'title': '독전'})
       print(tag)

       tag = bs.find('a')
       print(tag)

if __name__ == '__main__':
       ex3()
