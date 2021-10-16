from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from pprint import pprint

main_link = 'https://procharity.ru/'

html = requests.get(main_link + '/about_project/foundations_list/').text

parsed_html = bs(html, 'lxml')

funds_block = parsed_html.find('div', {'class': 'content bg-color-gray foundation-list'})
funds_list = funds_block.findAllNext(recursive=False)

pprint(len(funds_list))

funds = []
for fund in funds_list:
    fund_data = {}
    main_info = fund.find('div', {'class': 'col-lg-4 col-sm-4'})
    fund_name = main_info.getText().replace('\n', '').replace('  ', '')
    pprint(main_info)

    fund_info = main_link + main_info['href']

    print(fund_info)
    fund_info_get = requests.get(fund_info).text
    parsed_fund_info = bs(fund_info_get, 'lxml')
    fund_link = parsed_fund_info.find('div', {'class': 'block_about_found_info'}).findNextSibling()
    fund_link = fund_link.getText().replace('\n', '').replace(' ', '')

    fund_data['name'] = fund_name
    fund_data['link'] = fund_link

    funds.append(fund_data)

pprint(funds)
