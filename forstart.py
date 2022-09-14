import requests
from bs4 import BeautifulSoup
import re


def start_and_search_function():
    index_url = 'https://www.ptt.cc/bbs/index.html'
    response = requests.get(index_url, cookies={'over18': '1'})
    index_page = response.text
    soup = BeautifulSoup(index_page, 'lxml')
    top_10_board = soup.find_all(class_='board-name', limit=10)

    print('''
-----------------------------------------------
    ⭐︎⭐︎⭐︎Here are 10 popular boards！！⭐︎⭐⭐︎
    ⭐︎⭐But you can type what you want！！︎⭐︎⭐
-----------------------------------------------''')

    for each_board in top_10_board:
        each_board = each_board.text
        print(each_board.center(45))

    wanted_board_name = input('> ~~請輸入你想瀏覽的看版~~\n')

    check_url_loop = True
    while check_url_loop:
        url_target_board = f'https://www.ptt.cc/bbs/{wanted_board_name}/index.html'

        check_response = requests.get(url_target_board, cookies={'over18': '1'})
        web_for_check = check_response.text
        check_soup = BeautifulSoup(web_for_check, 'lxml')

        try:
            check_word = check_soup.find('div').text
            if re.search('Not Found', check_word):
                wanted_board_name = input('Please make sure the board name that you\'ve typed is correct\n>>')
            else:
                break
        except AttributeError:  # wanted_board_name變數中非常有意思，如果只有一個字 就會產生這個error
            check_word = check_soup.find('body').text
            if re.search('not found', check_word):
                wanted_board_name = input('Please make sure the board name that you\'ve typed is correct\n>>')
            else:
                break
    return url_target_board



