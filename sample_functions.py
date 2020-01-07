from gensim.models import FastText
import jieba.analyse as ja
import pandas as pd
import numpy as np




def tr(sent):
    return ja.textrank(sent, withWeight=True, topK=20, allowPOS=('ns', 'n', 'vn', 'v', 'x'))


from itertools import chain
import pprint


def get_sim_df(sets):
    sim_words = []
    score_words = []
    cent_words = []
    cent_words2 = []
    for word in sets:
        aa = model.wv.most_similar([word], topn=200)
        aa = list(zip(*aa))
        sim_words.append(list(aa[0]))
        score_words.append(list(aa[1]))
        cent_words.append(word)
        cent_words2.append(word + '_score')

    pp = []
    cols = []
    for i in range(len(sim_words)):
        pp.append(sim_words[i])
        pp.append(score_words[i])
        cols.append(cent_words[i])
        cols.append(cent_words2[i])

    df_sim = pd.DataFrame(pp).T
    df_sim.columns = cols

    words_dict = [dict(zip(sim_words[i], score_words[i])) for i in range(len(sim_words))]
    sim_dict = dict(zip(sets, words_dict))

    all_sim_words = list(set(list(chain(*sim_words))))
    df_sim = pd.DataFrame(sim_dict)
    return df_sim, all_sim_words


def sample_demo(thres):
    ss = 0
    write2txt = []
    while ss == 0:
        sample_sent = list(df.sample(n=1)['news_body'])[0]
        key_words = tr(sample_sent)
        key_words = list(zip(*key_words))
        if len(key_words) > 0:
            inter_words = list(set(list(key_words[0])).intersection(set(all_sim_words)))
        else:
            inter_words = []

        sets_dict = dict(zip(sets, [0] * len(sets)))
        why_words = []
        result = []
        for word in inter_words:
            dd = df_sim[df_sim.index == word]
            dd = dd.T
            dd = dd[~dd[word].isnull()]
            dd = dd.T
            keys = list(dd.keys())
            vals = list(dd.values[0])

            for i in range(len(keys)):
                result.append([list(dd.index)[0], round(vals[i], 2), list(dd.keys())[i]])
                sets_dict[keys[i]] += vals[i]
                why_words.append(
                    str(list(dd.index)[0]) + ' --- ' + str(round(vals[i], 2)) + ' --> ' + str(list(dd.keys())[i]))

        sets_dict = sorted(sets_dict.items(), key=lambda x: x[1], reverse=True)
        sets_dict = list(filter(lambda x: x[1] > 1, sets_dict))
        kks = [sets_dict[i][0] for i in range(len(sets_dict))]
        if len(sets_dict) > 0 and sets_dict[0][1] > thres and ss == 0:
            write2txt.append('*' * 50)
            write2txt.append('原文本')
            write2txt.append('-' * 50)
            write2txt.append(sample_sent)
            write2txt.append('\n')
            write2txt.append('*' * 50)
            write2txt.append('结果')
            write2txt.append('-' * 50)
            write2txt.append(sets_dict)
            write2txt.append('*' * 50)
            write2txt.append('\n')
            write2txt.append('*' * 50)
            write2txt.append('解释')
            write2txt.append('-' * 50)
            ss = 1
            # print('*'*50)
            # print('原文本')
            # print('-'*50)
            # print(sample_sent)
            # print('*'*50)
            # print('\n')
            # print('*'*50)
            # print('结果')
            # print('-'*50)
            # print(sets_dict)
            # print('*'*50)
            # print('\n')
            # print('*'*50)
            # print('解释')
            # print('-'*50)
            for i in range(len(why_words)):
                # print(why_words[i])
                write2txt.append(why_words[i])
            write2txt.append('\n')
            print('*' * 50)
    return result, write2txt
