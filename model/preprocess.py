import re
import os
import jieba
import pandas as pd


file_path = '../data/'
origin_file_name = 'train_crawl_data_0629_ltn.csv'
stopwords_file_path = 'stop_words.txt'
file_name = 'train_processed.csv'
cut_file_name = 'train.txt'


def get_stopwords():
    stopwords = [line.strip() for line in open(
        file_path + stopwords_file_path, 'r').readlines()]
    return stopwords


def csv_preprocess():
    df = pd.read_csv(file_path + origin_file_name)
    df = df.drop(index=0, axis=1)
    df['text'] = df['text'].replace(' ', '')
    df = df[df['text'].str.len() > 0]
    # pattern = re.compile('[^\u4e00-\u9fa5^a-z^A-Z^0-9]')
    pattern = re.compile('[^\u4e00-\u9fa5]')
    df['text'] = df['text'].apply(lambda x: re.sub(pattern, '', str(x)))
    df['text'].to_csv(file_path + file_name, index=False)


def text_process():
    result = ''
    stopwords = get_stopwords()
    with open(file_path + file_name, encoding='UTF-8') as f:
        for line in f.readlines():
            cutwords = jieba.lcut(line, cut_all=False)
            words = ''
            for word in cutwords:
                if word not in stopwords:
                    words += ' '.join(word)

            result += ' '.join(cutwords)
    with open(file_path + cut_file_name, 'w') as f:
        f.write(result)


csv_preprocess()
text_process()
