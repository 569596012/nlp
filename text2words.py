import pandas as pd
import numpy as np
import jieba
import jieba.posseg as jp
from gensim import corpora, models




base_dir = 'F:/DATA/News/'
news_file = 'news_data_1226.csv'
stock_relation_file = 'stock_att.csv'
user_words = 'user_words.txt'
stop_words = 'stopwords.txt'

# 加载词典
jieba.load_userdict(base_dir + user_words)

# 读取新闻数据
df = pd.read_csv(base_dir + news_file)
print('文本数量原始数量:', len(df))

# 丢弃缺失值
df = df.dropna(subset=['NEWS_BODY'])
print('根据缺失值过滤后数量:', len(df))

# 根据来源过滤
consider_sites = ['腾讯网', '和讯网', '金融界', '东方财富网', '新浪财经']
# consider_sites = ['和讯网']
df = df[df['NEWS_PUBLISH_SITE'].isin(consider_sites)]
print('根据来源过滤后数量:', len(df))

# 根据新闻长度过滤
df['body_len'] = df['NEWS_BODY'].apply(lambda x: len(x))
df = df[df['body_len'] > 50]
# df = df[df['body_len'] < 1000]
print('根据长度过滤后文本数量:', len(df))

texts = list(df['NEWS_BODY'])

# 停用词过滤
stopwords = open(base_dir + stop_words, 'r').readlines()
stopwords = [stopwords[i].strip('\n') for i in range(len(stopwords))] + [' ']

# 词性过滤
flags = ('n', 'nr', 'ns', 'nt', 'eng', 'v', 'd', 'x')


words_ls = []
cc = 0
for text in texts:
    words = [word.word for word in jp.cut(text) if word.flag in flags and word.word not in stopwords]
    words_ls.append(words)
    cc += 1
    if cc % 1000 == 0:
        print(cc)

df['words_ls'] = words_ls

<<<<<<< HEAD
df.to_csv('data/text2words.csv', index=False)
=======
df.to_csv('data/text2words.csv', index=False)
>>>>>>> aaa
