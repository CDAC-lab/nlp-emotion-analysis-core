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
    print(text)
    neg_word_list = NEGATION_MAP
    neg_match = False
    for neg_word in neg_word_list:
        if neg_word.strip() in text:
            neg_match = True
    print(neg_match)
    return neg_match



def check_intensifiers(text, INTENSIFIER_MAP):
    """
    Utility function to check intensifiers of an emotion
    :param text: text chunk with the emotion term
    :return: boolean value and booster value for intensifiers
    """
    # BOOSTER_MAP = {"B_INCR": 2,
    #                "B_DECR": 0.5}
    intensity_word_list = INTENSIFIER_MAP
    print(intensity_word_list)
    has_intensity = False
    booster = 'NULL'
    for int_term in intensity_word_list:
        intensifier = int_term.split(':')[0].strip()
        # print(intensifier)
        if intensifier in text:
            # print('yes')
            has_intensity = True
            booster = float(int_term.split(':')[2].strip())

    return has_intensity, booster


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
                         'afraid': 'trust',
                         'negative':'positive',
                         'positive': 'negative',
                         'model_strong': 'model_weak',
                         'model_weak': 'model_strong',
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


def get_empathetic_templates():
    templates = ['sorry to', 'sad to', 'sorry for', 'must be hard', 'sorry that', 'for you', 'QUE']
    return templates


def is_firstperson_post(sent_words):
    """
    Resolve pro noun use
    :param sent_words: sentence
    :return: first person post True/False
    """
    first_person_list = ['i', 'myself', 'me']
    second_person_list = ['you', 'yourself', 'your']
    i_count = 0
    you_count = 0
    match = False
    for term1 in sent_words:
        for i in first_person_list:
            if term1 == i:
                i_count += 1

    for term2 in sent_words:
        for j in second_person_list:
            if term2 == j:
                you_count += 1

    if i_count >= you_count:
        match = True
    return match