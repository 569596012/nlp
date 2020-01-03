import pandas as pd
import numpy as np
import jieba.posseg as jp
import jieba.analyse as anls
from gensim import corpora, models
from collections import defaultdict
from gensim.models import Word2Vec

base_dir = 'F:/DATA/News/'
news_file = 'news_data_1226.csv'
user_words = 'user_words.txt'
stop_words = 'stopwords.txt'
text_words_df = 'data1230.csv'
df = pd.read_csv(base_dir + text_words_df)

df['words_ls'] = df['words_ls'].apply(lambda x: eval(x))
texts = list(df['words_ls'])
print('文本数量:', len(texts))
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1] for text in texts]

dictionary = corpora.Dictionary(texts)

model = Word2Vec(texts, size=100, window=5, min_count=2, workers=4)
model.save('word2vec.model')

