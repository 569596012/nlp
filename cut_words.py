import os
import pandas as pd
import jieba
import jieba.posseg as jp

data_dir = 'F:/DATA/NewsData/'
file_name = 'all_news_data_0103.csv'
df = pd.read_csv(data_dir + file_name)

base_dir = 'F:/DATA/News/'
news_file = 'news_data_1226.csv'
stock_relation_file = 'stock_att.csv'
user_words = 'user_words.txt'
stop_words = 'stopwords.txt'

# 加载词典
jieba.load_userdict(base_dir + user_words)

# 停用词过滤
stopwords = open(base_dir + stop_words, 'r').readlines()
stopwords = [stopwords[i].strip('\n') for i in range(len(stopwords))] + [' ']

# 词性过滤
flags = ('n', 'nr', 'ns', 'nt', 'eng', 'v', 'd', 'x')

df = df[df['body_len'] < 512]
texts = list(df['news_body'])

words_ls = []
cc = 0
for text in texts:
    words = [word.word for word in jp.cut(text) \
             if word.flag in flags and word.word not in stopwords]
    words = ' '.join(words)
    words_ls.append(words)
    cc += 1
    if cc % 1000 == 0:
        print(cc)

df.to_csv(data_dir + 'corpus(100~512)_0103.csv', index=False)
words_ls = [words_ls[i] + '\n' for i in range(len(words_ls))]
open(data_dir + 'cut_words(100~512).txt', 'w', encoding='utf-8').writelines(words_ls)
