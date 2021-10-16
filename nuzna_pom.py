import time
from bs4 import BeautifulSoup as bs
from requests import Request, Session

url = 'https://nuzhnapomosh.ru/wp-content/plugins/nuzhnapomosh/funds.php'
search_words = 'орби'
request = Request('POST', url, files = {'np_name': (None, search_words)}).prepare()
session = Session()
response = session.send(request)
soup_nuzh = bs(response.text, 'html.parser')
org_list = soup_nuzh.find_all('div', class_='np-card__inner')

if len(org_list) != 0:
    for i in range(len(org_list)):
        name = org_list[i].h4.text

        descr = str(org_list[i].find('p', 'np-card__descr'))
        descr = descr.replace('<p class="np-card__descr">', '')
        descr = descr.replace('</p>', '')

        money = str(org_list[i].find('li', 'np-card__row'))
        money = money.split('<span>')[1]
        money = money.replace('</li>', '')
        money = money.replace(' ₽</span>', '')
        money = money.replace('\n', '')

        site = str(org_list[i].find('a', 'np-card__link'))
        site = site.replace('<a class="np-card__link" href="', '')
        site = site.split('"')[0]

        print(name + '\n' + descr + '\n' + 'Деньги в фонде: ' + money + ' Рублей' + '\n' + 'https://nuzhnapomosh.ru' + site + '\n')
else:
    print('Нет')