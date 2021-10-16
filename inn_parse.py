import requests
import time
from bs4 import BeautifulSoup as bs


def get_response(url):
    # start_time = time.time()
    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response
        time.sleep(2)


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
}
params = {
    'city': 'any',
    'recipient': 'all',
}

search_words = 'красивые дети'
params['query'] = search_words,
main_url = 'https://dobro.mail.ru'
url = 'https://dobro.mail.ru/funds/search/'

response = get_response(url)
soup = bs(response.text, 'html.parser')
funds_list = soup.find_all(class_='link_font_large')

fund_link = main_url + funds_list[0].attrs['href']

fund_link_response = get_response(fund_link)
fund_soup = bs(fund_link_response.text, 'html.parser')

fund_info_dict = {}
fund_info_dict['name'] = soup.find_all(class_='link__text')[0].text
fund_info_dict['phone'] = fund_soup.find_all(class_='p-fund-detail__info-cell')[1].text
fund_info_dict['url'] = fund_soup.find_all(class_='p-fund-detail__info-cell')[3].text

print(1)