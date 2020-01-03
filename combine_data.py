import os
import pandas as pd

data_dir = 'F:/DATA/NewsData/'

DataFiles = os.listdir(data_dir)
keep_cols = ['NEWS_ID', 'news_body', 'date',
             'NEWS_TITLE', 'NEWS_ORIGIN_SOURCE', 'body_len']
all_cols = list(pd.read_csv(data_dir + DataFiles[0], nrows=0, sep='\t').columns)
df = pd.DataFrame(columns=['NEWS_ID', 'news_body', 'date',
                           'NEWS_TITLE', 'NEWS_ORIGIN_SOURCE', 'body_len'])
for file in DataFiles:
    dd = pd.read_csv(data_dir + file, sep='\t')
    dd = dd.dropna(subset=['news_body', 'NEWS_PUBLISH_TIME', 'NEWS_ORIGIN_SOURCE'])
    dd['date'] = dd['NEWS_PUBLISH_TIME'].apply(lambda x: x[:10])
    dd['body_len'] = dd['news_body'].apply(lambda x: len(x))
    dd = dd[keep_cols]
    dd = dd[dd['body_len'] >= 100]
    dd = dd[dd['date'] > '2010-01-01']
    df = pd.concat([df, dd])
    print('file ' + file + ' finished')

df.to_csv(data_dir + 'all_news_data_0103.csv', index=False)
