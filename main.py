import re
import requests
from bs4 import BeautifulSoup
from navigator_button import *
from forstart import *
from url_shortener import *
from detect_number_and_words import *

index_of_the_index = 'https://www.ptt.cc'


def get_whole_page(current_url):
    response = requests.get(current_url, cookies={'over18': '1'})
    target_page = response.text
    target_soup = BeautifulSoup(target_page, 'lxml')
    articles = target_soup.find_all(class_ = 'r-ent')

    whole_page_elements = []
    sequence_counter = 0

    for article in articles:
        sequence_counter += 1
        page_elements = {
        'sequence_of_article': '-' + str(sequence_counter) + '-',
        'popularity': article.find('div', class_ = 'nrec').text,
        'title': article.find('div', class_ = 'title').text,
        'date': article.find('div', class_ = 'date').text,
        }
        try:
            page_elements['author'] = article.find('div', class_ = 'author').text
            if article.find('a') is None:
                page_elements['link'] = 'no link!'
            else:
                page_elements['link'] = index_of_the_index + article.find('a')['href']
        except AttributeError:
            title_text = page_elements['title'].text
            title_whole_content = page_elements['title']
            if '(本文已被刪除)' in title_whole_content:  # page_elements['title'].text 設成一個變數 簡潔code
                match_author = re.search('\[(\w*)\]', title_text)
                if match_author:
                    page_elements['author'] = match_author.group(1)
            elif '(本文已被刪除)' in title_whole_content:  # 40 44 依樣 要改 44無法進入 48 52 也是
                match_author = re.search('\<(\w*)\>', title_text)
                if match_author:
                    page_elements['author'] = match_author.group(1)
            elif re.search('已被\w*刪除', title_text) in title_whole_content:
                match_author = re.search('\[(\w*)\]', title_text)
                if match_author:
                    page_elements['author'] = match_author.group(1)
            elif re.search('已被\w*刪除', title_text) in title_whole_content:
                match_author = re.search('\<(\w*)\>', title_text)
                if match_author:
                    page_elements['author'] = match_author.group(1)
        whole_page_elements.append(page_elements)

    for calculator_of_print in whole_page_elements:
        print('{:4}'.format(calculator_of_print['sequence_of_article']),
              '{:3}'.format(calculator_of_print['popularity']),
              '{:40}'.format(calculator_of_print['title'].strip()),  # there are some /n and /t in the front and back
              '{:5}'.format(calculator_of_print['date']),
              '{:>}'.format(calculator_of_print['author']))

    order_from_user = input('''>> Type the number between '- -' to get the url of the certain article...
>> Or you can browse other pages if you want
>> (By typing 'next/previous/oldest/latest')
''')

    if detect_whether_number(order_from_user):
        need_to_print = True
        while need_to_print:
            order_from_user = int(order_from_user) - 1
            try:
                link_of_target_article = whole_page_elements[order_from_user]['link']
                if link_of_target_article == 'no link!':
                    order_from_user = input('That article has been deleted! please try other number\n')
                else:
                    url_shortener(link_of_target_article)
                    break
            except (IndexError, ValueError):
                order_from_user = input('Oops! there\'s something wrong! Try a smaller number without any alphabet\n')
    else:
        new_page_url = get_function_buttons(current_url, order_from_user)
        get_whole_page(new_page_url)


current_page_url = start_and_search_function()
get_whole_page(current_page_url)

