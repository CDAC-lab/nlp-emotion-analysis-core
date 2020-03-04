"""
Date: 2/27/2020 5:59 PM
Author: Achini
"""


def check_negation(text, NEGATION_MAP):
    """
    Utility function to check negation of an emotion
    :param text: text chunk with the emotion term
    :return: boolean value for negation
    """
    neg_word_list = NEGATION_MAP
    neg_match = False
    for neg_word in neg_word_list:
        if neg_word.strip() in text:
            neg_match = True

    return neg_match


def check_intensifiers(text, INTENSIFIER_MAP):
    """
    Utility function to check intensifiers of an emotion
    :param text: text chunk with the emotion term
    :return: boolean value for intensifiers
    """

    intensity_word_list = INTENSIFIER_MAP
    has_intensity = False
    for int_word in intensity_word_list:
        if int_word.strip() in text:
            has_intensity = True

    return has_intensity


def get_opposite_emotion(key):
    """
    Utility function to get the opposite emotion of a given emotion
    :param key: emotion to be processed
    :return: opposite emotion, None if no opposite emotion is found
    """
    opposite_emotions = {"joy": "anger",
                         "sad": "joy",
                         "anticipation": "anger",
                         "trust": "fear",
                         'fear': 'trust',
                         'anger' : 'joy',
                         'afraid': 'trust'
                         }

    if opposite_emotions.keys().__contains__(key):
        return opposite_emotions[key]
    else:
        return None


def get_sentiment_of_emotions(emotion):
    """
    Utility function to get the POS/NEG categorization of an emotion
    :param emotion: emotion to be processed
    :return: POS, NEG category
    """
    POS = ['joy', 'trust', 'anticipation', 'surprise']
    NEG = ['sad', 'fear', 'disgust', 'anger', 'hopelessness', 'loneliness', 'distress']

    if emotion in POS:
        return 'POS'
    elif emotion in NEG:
        return 'NEG'
    else:
        return None
