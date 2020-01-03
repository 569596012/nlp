import pandas as pd
import numpy as np
import jieba.posseg as jp,jieba
import jieba.analyse as anls
from gensim import corpora, models

base_dir = 'F:/DATA/News/'
news_file = 'news_data_1226.csv'
stock_relation_file = 'stock_att.csv'
user_words = 'user_words.txt'
stop_words = 'stopwords.txt'

df = pd.read_csv(base_dir + stock_relation_file)\

print(df)