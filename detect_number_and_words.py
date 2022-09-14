import re


def detect_whether_number(detect_input_from_numbers):
    if re.search('^\d+$', detect_input_from_numbers):
        result_of_number_status = True
    else:
        result_of_number_status = False
    return result_of_number_status


def detect_whether_words(detect_input_from_words):
    if re.search('[A-Za-z]', detect_input_from_words):
        result_of_words_status = True
    else:
        result_of_words_status = False
    return result_of_words_status


def detect_whether_match_navigator_button(detect_input_from_matching):
    detect_input_from_matching.lower()
    whether_input_is_correct = True
    while whether_input_is_correct:
        if detect_input_from_matching == 'latest':
            break
        elif detect_input_from_matching == 'oldest':
            break
        elif detect_input_from_matching == 'previous':
            break
        elif detect_input_from_matching == 'next':
            break
        elif not detect_whether_words(detect_input_from_matching):
            detect_input_from_matching = input('Oops, there\'re something wrong, please type again \n>>')
        else:
            detect_input_from_matching = input('Oops, there\'re something wrong, please type again \n>>')
    return detect_input_from_matching

