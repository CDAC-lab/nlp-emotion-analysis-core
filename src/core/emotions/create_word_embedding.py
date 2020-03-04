# imports needed and set up logging
import gensim
import logging
import pandas as pd
from nltk.tokenize import word_tokenize
import string
import src.utils.text_processor as text_utils


def create_wordembedding_model(posts, model_name, test_word):
    """
    Function to create a word2vec embedding model
    :param posts: training data
    :param model_name: name to save the word embedding model
    :param test_word: test word to query the trained model
    :return: trained word embedding model
    """
    documents = []
    for post in posts:
        documents.append(word_tokenize(post))
    print('data processing completed')

    """ create word embedding model """
    model = gensim.models.Word2Vec(documents, size=100, window=10, min_count=2, workers=10)
    model.train(documents, total_examples=len(documents), epochs=10)

    print('-----training complete--------')

    model.save(model_name)
    print('-----model saved-------------')

    w1 = test_word
    print(model.wv.most_similar(positive=w1))

    return model


if __name__ == '__main__':

    data_path = 'enter data path here'
    model_name = 'we_emotions.model'
    test_word = 'sad'

    df = pd.read_csv(data_path)
    posts = df['post'].apply(text_utils.clean_text)
    word2vec_model = create_wordembedding_model(posts, model_name, test_word)
