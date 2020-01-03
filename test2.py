import pandas as pd
import numpy as np
import jieba.posseg as jp
import jieba.analyse as anls
from gensim import corpora, models
from pprint import pprint

model = models.Word2Vec.load('word2vec.model')


base_dir = 'F:/DATA/News/'
df = pd.read_csv(base_dir + 'data1230.csv')
df['words_ls'] = df['words_ls'].apply(lambda x: eval(x))


test_words = ['华为', '5G', '人工智能', '语音识别', '人脸识别', '生物制药', '制药', '疫苗']
for word in test_words:
    df[word + ' in text'] = df['words_ls'].apply(lambda x: word in x)

test_words_cols = [test_words[i] + ' in text' for i in range(len(test_words))]
df['if in text'] = df[test_words_cols].apply(lambda x: sum(x) > 0, axis=1)
print(df)
