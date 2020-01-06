import os
import re

base_dir = 'F:/DATA/data_0106/stopwords-master/'
files = os.listdir(base_dir)
files = list(filter(lambda x: x.endswith('.txt'), files))

words = []
for file in files:
    try:
        word = open(base_dir + file, 'r', encoding='utf-8').readlines()
    except:
        word = open(base_dir + file, 'r', encoding='gbk').readlines()
    print(file, '    长度:', len(word))
    words.append(word)

words = list(set(list(chain(*words))))
print('合并去重后:    ', len(words))

open(base_dir + 'merged_stopwords.txt', 'w', encoding='utf-8').writelines(words)