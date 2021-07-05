import sys

from srcs.Calculation import calc_tf, calc_idf, calc_tfidf
from srcs.utils import read_bz2, print_result


def main(bz2file):
    print(f'read {bz2file}')
    docs = read_bz2(bz2_path)
    print('Calculating tf.')
    tf, inverted_index = calc_tf(docs)
    print('Calculating idf')
    idf = calc_idf(tf)
    print('Calculating tf-idf')
    tf_idf = calc_tfidf(tf, idf)
    print_result(tf_idf, inverted_index)
    print('Done!')


if __name__ == '__main__':
    args = sys.argv
    bz2_path = args[1]
    main(bz2_path)
