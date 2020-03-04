"""
Date: 9/6/2019 4:45 PM
Author: Achini
"""

import gensim
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity
from scipy import spatial


def similarity_between_emotions(model):
    """
    Function to calculate the similarity metrics between emotions and create a heatmap
    :param model: trained model
    :return: None
    """
    csv = []
    headings = ['emotion', 'target', 'value']
    csv.append(headings)
    for e1 in EMOTIONS:
        for e2 in EMOTIONS:
            s = model.wv.similarity(e1, e2)
            csv.append([e1, e2, s])

    pd.DataFrame(csv).to_csv(RESULT_ROOT + 'heatmap.csv')


def tsne_plot_similar_words(title, labels, embedding_clusters, word_clusters, a, filename):
    """
    Function to visualize the related terms in 2d space using tsne, and to write the related terms to a csv
    :param title: title of the image
    :param labels: keys (emotions)
    :param embedding_clusters: embedding_clusters from the we model
    :param word_clusters: word_clusters from the we model
    :param a: alpha for the plot.annotate function
    :param filename: filename for the figure
    :return: None
    """
    plt.figure(figsize=(16, 9))
    colors = cm.rainbow(np.linspace(0, 1, len(labels)))
    for label, embeddings, words, color in zip(labels, embedding_clusters, word_clusters, colors):
        csv = []
        x = embeddings[:, 0]
        y = embeddings[:, 1]
        plt.scatter(x, y, c=color, alpha=a, label=label)
        for i, word in enumerate(words):
            plt.annotate(word, alpha=0.9, xy=(x[i], y[i]), xytext=(5, 2),
                         textcoords='offset points', ha='right', va='bottom', size=8)
            csv.append([label, word])
        """ write output to csv"""
        pd.DataFrame(csv).to_csv(RESULT_ROOT + label + '.csv')
    plt.legend(loc=4)
    plt.title(title)
    plt.grid(False)

    plt.savefig(filename, format='png', dpi=1200, bbox_inches='tight')
    plt.show()
    pd.DataFrame(csv).to_csv(RESULT_ROOT + 'model_outcomes.csv')


def query_similar_terms(model, keys, figure_name):
    """
    Function to query similar terms for a set of emotions
    :param model: trained word2vec model
    :param keys: words to be queried
    :return: None
    """

    embedding_clusters = []
    word_clusters = []
    for word in keys:
        embeddings = []
        words = []
        for similar_word, _ in model.most_similar(word, topn=30):
            words.append(similar_word)
            embeddings.append(model[similar_word])
        embedding_clusters.append(embeddings)
        word_clusters.append(words)

    embedding_clusters = np.array(embedding_clusters)
    n, m, k = embedding_clusters.shape
    tsne_model_en_2d = TSNE(perplexity=15, n_components=2, init='pca', n_iter=3500, random_state=32)
    embeddings_en_2d = np.array(tsne_model_en_2d.fit_transform(embedding_clusters.reshape(n * m, k))).reshape(n, m, 2)

    tsne_plot_similar_words('Similar words', keys, embeddings_en_2d, word_clusters, 0.7,
                             figure_name)


if __name__ == '__main__':
    model = gensim.models.Word2Vec.load('model_name')
    RESULT_ROOT = 'path to save output'
    figure_name = RESULT_ROOT + 'sample.png'

    EMOTIONS = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sad', 'surprise', 'trust']

    """ tsne """
    query_similar_terms(model, EMOTIONS, figure_name)

    """ similarity """
    compute_similarity_two_vectors(MODEL)