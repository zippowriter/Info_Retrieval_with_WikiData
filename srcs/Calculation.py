import math

import spacy


def calc_tf(entries):
    tf = {}
    inverted_index = {}
    nlp = spacy.load("en_core_web_sm")
    for entry, text in entries.items():
        w = {}
        doc = nlp(text)
        for d in doc:
            if d.text.lower() not in inverted_index.keys():
                inverted_index[d.text.lower()] = []
            if d.pos_ == "NOUN" or d.pos_ == "VERB" or d.pos_ == "ADJ":
                if d.text.lower() in w.keys():
                    w[d.text.lower()] += 1
                else:
                    w[d.text.lower()] = 1
                    inverted_index[d.text.lower()].append(entry)
        tf[entry] = w

    return tf, inverted_index


def calc_idf(tf):
    idf = {}
    doc_num = len(tf)
    for w in tf.values():
        for word in w.keys():
            if word not in idf.keys():
                count = 0
                for content in tf.keys():
                    if word in tf[content].keys():
                        count += 1
                idf[word] = math.log(doc_num / count) + 1
            else:
                pass

    return idf


def calc_tfidf(tf, idf):
    tfidf_dic = {}
    for content, w in tf.items():
        tf_idf = {}
        for word, count in w.items():
            tf_idf[word] = count * idf[word]
        tfidf_dic[content] = tf_idf

    return tfidf_dic
