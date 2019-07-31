import requests
from bs4 import BeautifulSoup

all_txt = []
all_idx = 1

for i in range(0, 10):
    ret = requests.get(
        url="https://maoyan.com/board/4?offset=%d" % (i * 10)
    )

    ret.encoding = ret.apparent_encoding
    soup = BeautifulSoup(ret.text, 'html.parser')
    dl = soup.find('dl', class_="board-wrapper")

    for item in dl.find_all('dd'):
        info = item.find('div', class_="movie-item-info")
        name = info.find('a').text
        star = info.find('p', class_='star').text.strip().strip('主演：')
        time = info.find('p', class_='releasetime').text.strip('上映时间：')
        all_txt.append('{}\t{:15}\t{:15}\t{}'.format(all_idx, name, time, star))

        imgsrc = item.find('img', class_='board-img')['data-src']
        imgname = str(all_idx) + '.jpg'
        with open(imgname, "wb") as f:
            imgret = requests.get(url=imgsrc)
            f.write(imgret.content)

        all_idx = all_idx + 1

with open('news.txt', 'wb') as f:
    f.write(bytes('\r\n'.join(all_txt), 'utf8'))
