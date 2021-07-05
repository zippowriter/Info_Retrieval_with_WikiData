import bz2
import json


def read_bz2(bz2file):
    with bz2.open(bz2file, mode='rt') as f:
        data = f.read()
        data = data.replace('\n', '\t')

    split_data = data.split('\t')
    it = iter(split_data)

    entry_and_text = {}
    for entry, text in zip(it, it):
        entry_and_text[entry] = text

    return entry_and_text


def print_result(tfidf, inverted_index):
    with open('tfidf.json', 'w') as f:
        tfidf_result = json.dumps(tfidf, indent=4)
        f.write(tfidf_result)

    with open('inverted_index.json', 'w') as f:
        inverted_index_result = json.dumps(inverted_index, indent=4)
        f.write(inverted_index_result)


def load_json(tfidf_file, inverted_index_file):
    with open(tfidf_file) as f:
        tfidf = json.load(f)

    with open(inverted_index_file) as f:
        inverted_index = json.load(f)

    return tfidf, inverted_index
