import sample_functions as functions
from gensim.models import FastText
import jieba.analyse as ja
import pandas as pd
import numpy as np
from itertools import chain
import pprint

# 加载stopwords
stopwords_file = 'F:/DATA/data_0106/stopwords-master/merged_stopwords.txt'
ja.set_stop_words(stopwords_file)

# 读取文本数据
data_dir = 'F:/DATA/NewsData/'
file_name = 'all_news_data_0103.csv'
df = pd.read_csv(data_dir + file_name)
df = df[df['body_len'] < 1024]

# load 模型
base_dir = 'F:/DATA/models/'
model_file = 'model_0107/fasttext.model'
model = FastText.load(base_dir + model_file)

# 设置待选集
sets = ['人工智能', '5G', '半导体', '港口', '疫苗',
        '自贸区', '智能家居', '网络游戏', '家用电器', '融资融券',
        '电商', '房地产开发', '食品', '宏观政策', '基建',
        '手机', '券商', '银行', '保险', '外汇',
        'P2P', '医疗', '节能', '节能', '分红',
        '电池', '能源', '电力', '交通', '养殖']

# 计算相似词矩阵，df格式
df_sim, all_sim_words = functions.get_sim_df(model, sets)

write2txts = []
count = 0
thres = 1.5
while count < 500:
    result, write2txt = functions.sample_demo(df, df_sim, all_sim_words, sets, thres)
    write2txt = [str(write2txt[i]) + '\n' for i in range(len(write2txt))]
    write2txt = ['第' + str(count) + '个样例\n'] + write2txt
    write2txts = write2txts + write2txt
    count += 1
    print(count)

write_file = 'F:/DATA/data_0107/'
open(write_file + 'test_samples_2.txt', 'w', encoding='utf-8').writelines(write2txts)
