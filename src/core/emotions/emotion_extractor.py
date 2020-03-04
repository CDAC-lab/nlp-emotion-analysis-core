"""
Date: 2/27/2020 5:58 PM
Author: Achini
"""

import re
import src.core.emotions.emotion_utilities as emotion_utils


def get_emotion_profile_per_post(clean_post, EMO_RESOURCES):
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
    post_len = len(sent_words)

    for key in EMOTION_MAP.keys():
        for emoWord in EMOTION_MAP[key]:
            try:
                emoWord = emoWord.strip().lower()
                matched_emotion = emoWord.strip().lower()

                if len(emoWord.split()) > 1:
                    pattern = re.compile(r'\b%s\b' % emoWord, re.I)
                    match_found = pattern.search(clean_post)
                else:
                    match_found = emoWord in sent_words

                if match_found:
                    selected_emo = key

                    """ handle intensifiers"""
                    if len(emoWord.split()) > 1:
                        emoWord = emoWord.split()[0]
                    end_ind_int = sent_words.index(emoWord)
                    start_ind_int = end_ind_int - 2
                    text_chunk_int = sent_words[start_ind_int:end_ind_int]
                    intensity = emotion_utils.check_intensifiers(text_chunk_int, INTENSIFIER_MAP)

                    """ handle negation """
                    end_ind = sent_words.index(emoWord)
                    if end_ind < 2:
                        start_ind = 0
                    else:
                        start_ind = end_ind - 2
                    text_chunk = sent_words[start_ind:end_ind]
                    negation = emotion_utils.check_negation(text_chunk, NEGATION_MAP)
                    if negation:
                        # get opposite emotion
                        selected_emo = emotion_utils.get_opposite_emotion(key)
                    if selected_emo is not None:
                        emo_value = 1
                        all_emo_words.append(matched_emotion)
                        if intensity:
                            emo_value = 2
                        if emo_counts.get(selected_emo) is not None:
                            current_count = emo_counts.get(selected_emo)
                            emo_counts[selected_emo] = current_count + emo_value
                        else:
                            emo_counts[selected_emo] = emo_value

                    emo_seq.append(selected_emo)
            except:
                emo_counts[key] = 0

        if emo_counts.get(key) is None:
            emo_counts[key] = 0
        if post_len > 0:
            emotion_profile[key] = emo_counts[key] / post_len
        else:
            emotion_profile[key] = 0

    return emotion_profile


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
        post_profile = get_emotion_profile_per_post(post, EMO_RESOURCES)
        for e in post_profile:
            agg_profile[e] = agg_profile[e] + post_profile[e]

            if emotion_utils.get_sentiment_of_emotions(e) == 'POS':
                agg_POS += post_profile[e]
            elif emotion_utils.get_sentiment_of_emotions(e) == 'NEG':
                agg_NEG += post_profile[e]

    agg_sum = {'aggPOS': agg_POS, 'aggNEG': agg_NEG}

    return agg_profile, agg_sum