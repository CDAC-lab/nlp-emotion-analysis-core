"""
Date: 2/27/2020 6:01 PM
Author: Achini
"""
import re
import string


""" define custom templates to ignore in posts"""
TEMPLATES = ['good morning', 'good afternoon', 'good night', 'good evening']


def clean_text(post):
    """
    Function to filter basic greetings and clean the input text.
    :param post: raw post
    :return: clean_post or None if the string is empty after cleaning
    """
    post = str(post)

    """ filtering basic greetings """
    for template in TEMPLATES:
        if template in str(post).lower():
            post = post.replace(template, '')

    """ clean text """
    raw_text = str(post).replace('\'', ' ')
    translator = re.compile('[%s]' % re.escape(string.punctuation))
    clean_text_sub = translator.sub(' ', raw_text)
    clean_text = re.sub(' +', ' ', clean_text_sub).strip()

    if clean_text == 'nan' or clean_text is None:
        return ''
    else:
        return clean_text
