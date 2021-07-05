import json

import numpy as np


def word2id(inverted_index):
    word_id = {}
    for idx, key in enumerate(inverted_index.keys()):
        word_id[key] = idx

    return word_id


def search_doc(query, word_id, inverted_index, tfidf):
    doc_vec = {}
    query_vec = {}
    cos_sim = {}
    vec_len = len(inverted_index)
    try:
        doc_list = inverted_index[query]
    except Exception:
        print('This query is not found.')
        exit(1)

    def cos_similarity(x, y):
        return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

    for doc in doc_list:
        doc_vec[doc] = np.zeros(vec_len)
        query_vec[doc] = np.zeros(vec_len)
        query_vec[doc][word_id[query]] = tfidf[doc][query]

        for word in tfidf[doc].keys():
            doc_vec[doc][word_id[word]] = tfidf[doc][word]

        cos_sim[doc] = cos_similarity(query_vec[doc], doc_vec[doc])
        print(f"{doc} : {cos_sim[doc]:.5f}")
