"""
Date: 2/27/2020 5:58 PM
Author: Achini
"""
from nltk.stem import PorterStemmer

porter = PorterStemmer()
import re
import src.core.emotions.emotion_utilities as emotion_utils
from nltk.tokenize import sent_tokenize
import src.utils.text_processor as text_utils
import operator


def get_emotion_profile_per_post(clean_post, EMO_RESOURCES):
    # print('viola')
    """
    Function to process each post to extract emotion mentions
    :param clean_post: post to be processed
    :return emotion_profile (dictionary): dictionary containing the intensity for each emotion
    """
    EMOTION_MAP = EMO_RESOURCES['EMOTIONS']
    NEGATION_MAP = EMO_RESOURCES['NEGATION']
    INTENSIFIER_MAP = EMO_RESOURCES['INTENSIFIERS']

    emotion_profile = {}
    emo_counts = {}
    all_emo_words = []
    emo_seq = []

    sent_words = str(clean_post).lower().split()
    print('sent_words',sent_words)
    sent_words_st = [porter.stem(wd) for wd in sent_words]
    print('sent_words', sent_words)
    print(EMOTION_MAP)
    # print(len(EMOTION_MAP['anger']))
    post_len = len(sent_words)
    """ emotion extraction """
    # try:
    for key in EMOTION_MAP.keys():
        emotion_profile[key] = []
    for key in EMOTION_MAP.keys():

        for emoWord in EMOTION_MAP[key]:
            try:
                emoWord = emoWord.strip().lower()
                matched_emotion = emoWord.strip().lower()

                if len(emoWord.split()) > 1:
                    pattern = re.compile(r'\b%s\b' % emoWord, re.I)
                    print(clean_post)
                    clean_post = (' ').join(sent_words_st)
                    match_found = pattern.search(clean_post)

                else:
                    match_found = emoWord in sent_words_st


                if match_found:
                    selected_emo = key
                    all_emo_words.append(emoWord)

                    """ handle intensifiers"""
                    # print('intense')
                    if len(emoWord.split()) > 1:
                        emoWord = emoWord.split()[0]
                    end_ind_int = sent_words_st.index(emoWord)
                    start_ind_int = end_ind_int - 3
                    if start_ind_int < 0:
                        start_ind_int = 0
                    text_chunk_int = sent_words[start_ind_int:end_ind_int]
                    has_intensity, booster = emotion_utils.check_intensifiers(text_chunk_int, INTENSIFIER_MAP)
                    # print('has int',has_intensity)
                    """ handle negation """
                    print('negate')
                    end_ind = sent_words_st.index(emoWord)
                    if end_ind < 3:
                        start_ind = 0
                    else:
                        start_ind = end_ind - 3
                    text_chunk = sent_words[start_ind:end_ind]
                    negation = emotion_utils.check_negation(text_chunk, NEGATION_MAP)
                    if negation:
                        # get opposite emotion
                        print(negation)
                        selected_emo = emotion_utils.get_opposite_emotion(key)
                        print(selected_emo)


                    """ handle empathy """
                    if key == 'sad':
                        templates = emotion_utils.get_empathetic_templates()
                        for temp in templates:
                            pattern = re.compile(r'\b%s\b' % temp, re.I)
                            clean_post = (' ').join(sent_words_st)
                            empath_match = pattern.search(clean_post)
                            if empath_match is not None:
                                selected_emo = None
                            else:
                                firstperson = emotion_utils.is_firstperson_post(sent_words)
                                if not firstperson:
                                    selected_emo = None

                    """ assign value """
                    if selected_emo is not None:
                        print('yes',selected_emo)
                        emo_value = 1
                        emo_seq.append(selected_emo)
                        if has_intensity:
                            emo_value = 1 * booster
                        else:
                            emo_value = 1 * 0.5
                    else:
                        emo_value = 0
                    emotion_profile[selected_emo].append(emo_value)

            except Exception as e:
                print('exception')
                print(e)

        emotion_profile[key] = sum(emotion_profile[key])

    return emotion_profile, emo_seq


def get_emotion_sequence(posts, EMO_RESOURCES):
    emo_seq = []
    agg_profile = {}

    for post in posts:
        clean_post = text_utils.clean_text(post)
        sentences = sent_tokenize(clean_post)

        for sent in sentences:
            profile, seq = get_emotion_profile_per_post(sent, EMO_RESOURCES)
            if profile != {}:
                max_emotion = max(profile.items(), key=operator.itemgetter(1))[0]
                max_emo_val = max(profile.items(), key=operator.itemgetter(1))[1]

            if max_emo_val > 0:
                for key in profile:
                    if profile[key] == max_emo_val:
                        emo_seq.append(max_emotion)
                    if key in agg_profile.keys():
                        agg_profile[key] = agg_profile[key] + profile[key]
                    else:
                        agg_profile[key] = profile[key]

    return emo_seq, agg_profile


def get_aggregated_emotions(all_posts, EMO_RESOURCES):
    """
    Function to get the aggregated emotions
    :param all_posts: all posts in a session/user
    :return: (dictionary) agg_profile with intensities for granular emotions,
             (dictionary) agg_sum with aggregated POS/NEG intensities
    """
    agg_profile = {}
    agg_POS = 0.0
    agg_NEG = 0.0
    for KEY in EMO_RESOURCES['EMOTIONS'].keys():
        agg_profile[KEY] = 0.0

    for post in all_posts:
        try:
            post_profile = get_emotion_profile_per_post(post, EMO_RESOURCES)
            for e in post_profile:
                agg_profile[e] = agg_profile[e] + post_profile[e]

                if emotion_utils.get_sentiment_of_emotions(e) == 'POS':
                    agg_POS += post_profile[e]
                elif emotion_utils.get_sentiment_of_emotions(e) == 'NEG':
                    agg_NEG += post_profile[e]
        except:
            post_profile = {}

    agg_sum = {'aggPOS': agg_POS, 'aggNEG': agg_NEG}

    return agg_profile, agg_sum
