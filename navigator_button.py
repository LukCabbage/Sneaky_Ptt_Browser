import re
import requests
from bs4 import BeautifulSoup
from detect_number_and_words import *


index_of_the_index = 'https://www.ptt.cc'


def get_function_buttons(url_of_current_page, wanted_button):
    wanted_button.lower()
    temporary_url = url_of_current_page
    response = requests.get(temporary_url, cookies={'over18': '1'})
    target_page_from_navigator_button = response.text
    function_buttons = BeautifulSoup(target_page_from_navigator_button, 'lxml')

    wanted_button = detect_whether_match_navigator_button(wanted_button)

    while wanted_button == 'latest' or 'oldest' or 'previous' or 'next':
        if wanted_button == 'latest':
            wanted_direction = index_of_the_index + function_buttons.find('a', text=re.compile('最新')).get('href')
            break

        elif wanted_button == 'oldest':
            wanted_direction = index_of_the_index + function_buttons.find('a', text=re.compile('最舊')).get('href')
            break

        elif wanted_button == 'previous':
            if function_buttons.find('a', text=re.compile('‹ 上頁')).get('href') is None:
                print('You are currently watching the oldest page of this board!!\n')
                wanted_button = input('Try again and make sure your direction \n>>')

            elif function_buttons.find('a', text=re.compile('‹ 上頁')).get('href'):
                wanted_direction = index_of_the_index + function_buttons.find('a', text=re.compile('‹ 上頁')).get('href')
                break

        elif wanted_button == 'next':
            if function_buttons.find('a', text=re.compile('下頁 ›')).get('href') is None:
                print('You are currently watching the newest page of this board!!')
                wanted_button = input('Try again and make sure your direction \n>>')

            elif function_buttons.find('a', text=re.compile('下頁 ›')).get('href'):
                wanted_direction = index_of_the_index + function_buttons.find('a', text=re.compile('下頁 ›')).get('href')
                break

    return wanted_direction
