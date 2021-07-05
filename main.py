import sys

from srcs.Search import word2id, search_doc
from srcs.utils import load_json


def main(tfidf, inverted_index, query):
    word_id = word2id(inverted_index)
    search_doc(query, word_id, inverted_index, tfidf)


if __name__ == '__main__':
    args = sys.argv
    query = args[1]
    tfidf_json = 'tfidf.json'
    inverted_index_json = 'inverted_index.json'
    tfidf, inverted_index = load_json(tfidf_json, inverted_index_json)
    main(tfidf, inverted_index, query)
