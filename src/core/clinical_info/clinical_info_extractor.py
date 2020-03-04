"""
Date: 2/28/2020 10:51 AM
Author: Achini
"""

import re


def get_physical_sym_profile(posts, EMO_RESOURCES):
    """
    Function to extract mentions of physical symptoms
    :param post: clean post
    :return: dictionary containing physical symptom score (number) and mentions (list)
    """
    PHYSICAL_MAP = EMO_RESOURCES['PHYSICAL']
    num_posts = len(posts)
    physical_terms = {}
    if type(posts) is str:
        posts = [posts]
    for post in posts:
        try:
            sent_words = str(post).lower().split()
            for term in PHYSICAL_MAP:
                term = term.strip().lower()

                if len(term.split()) > 1:
                    pattern = re.compile(r'\b%s\b' % term, re.I)
                    match_found = pattern.search(post)
                else:
                    match_found = term in sent_words
                if match_found:
                    if term in physical_terms.keys():
                        physical_terms[term] = physical_terms[term] + 1
                    else:
                        physical_terms[term] = 1
        except:
            match_found = False

    if num_posts > 0:
        for key in physical_terms.keys():
            physical_terms[key] = physical_terms[key] / num_posts

    return physical_terms
