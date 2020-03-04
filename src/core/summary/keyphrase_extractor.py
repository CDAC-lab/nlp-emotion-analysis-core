"""
Date: 2/29/2020 8:51 PM
Author: Achini
"""
import src.core.summary.rake as RAKE


def combine_posts(posts):
    """
    Function to combine posts to single text
    :param posts: all posts by a user
    :return: (String) combined text
    """
    combined_text = '.'.join(posts)
    return combined_text


def analyze_keyphrases(posts):
    """
    Function to extract key phrases in a set of posts, done using RAKE (Rose, S., D. Engel, N. Cramer, and W. Cowley (2010).)
    :param posts: all posts of a user
    :return: (dictionary) high frequent key phrases
    """
    if type(posts) is not str:
        text = combine_posts(posts)
    else:
        text = posts
    keywords = RAKE.rake.run(text)
    high_freq_keywords = []
    for pair in keywords:
        """ set threshold to select keyphrases """
        try:
            if pair[1] > 3.5:
                high_freq_keywords.append([pair[0], pair[1]])
        except IndexError:
            continue
    return high_freq_keywords
