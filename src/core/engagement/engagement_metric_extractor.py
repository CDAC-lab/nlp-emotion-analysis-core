"""
Date: 2/28/2020 6:47 PM
Author: Achini
"""
import src.core.emotions.emotion_extractor as emotions
from statistics import mean


def get_emotion_engagement_score(posts_list, EMO_RESOURCES):
    """
    Function to calculate emotion enagement
    :param posts_list: post list of a user
    :return: emotion_engagement_score
    """
    """ get emotion-less posts """
    emotion_values = []
    all_emotion_profiles = []
    emotion_less_posts = 0
    highly_emotional_posts = 0

    for post in posts_list:
        emotion_profile = emotions.get_emotion_profile_per_post(post, EMO_RESOURCES)
        if sum(emotion_profile.values()) == 0:
            emotion_less_posts += 1

        for val in emotion_profile.values():
            emotion_values.append(val)

        all_emotion_profiles.append(emotion_profile.values())

    emotion_mean = mean(emotion_values)

    """ get highly emotional posts """
    for emo_value_profile in all_emotion_profiles:
        if sum(emo_value_profile) > emotion_mean:
            highly_emotional_posts += 1

    if emotion_less_posts > 0:
        emotion_engagement_score = highly_emotional_posts / emotion_less_posts

    else:
        emotion_engagement_score = highly_emotional_posts

    return emotion_engagement_score


def get_participation_score(user_posts, all_posts, num_all_users):
    """
    Function to calculate the relative participation score
    :param user_posts: (list) posts of a user
    :param all_posts: (list) all posts
    :param num_all_users: (int) number of users
    :return: (number) participation score
    """
    user_post_len = 0
    all_post_len = 0
    num_user_posts = len(user_posts)
    num_all_posts = len(all_posts)

    """ calculate average post length of a user """
    for u_post in user_posts:
        user_post_len += len(u_post.split())
    if num_user_posts > 0:
        avg_post_len_USER = user_post_len / num_user_posts
    else:
        avg_post_len_USER = 0

    """ calculate average post length of the group """
    for post in all_posts:
        all_post_len += len(post.split())
    if num_all_posts > 0:
        avg_post_len_ALL = all_post_len / num_all_posts
    else:
        avg_post_len_ALL = 0

    """ average length of post - relative measure """
    if avg_post_len_ALL > 0:
        avg_post_len = avg_post_len_USER / avg_post_len_ALL
    else:
        avg_post_len = 0

    """ average number of posts - relative measure """
    if (num_all_posts / num_all_users) > 0:
        avg_posts_by_user = num_user_posts / (num_all_posts / num_all_users)
    else:
        avg_posts_by_user = 0

    """ overall participation score """
    participation_score = avg_post_len * avg_posts_by_user

    return participation_score
