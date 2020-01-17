import pandas as pd
import numpy as np
import datetime
import random

base_dir = 'F:/DATA/NewsData/'
df = pd.read_csv(base_dir + 'all_news_data_0103.csv')

cut_date = '2018-01-01'
df1 = df[df['date'] < cut_date].sample(n=30000)
df2 = df[df['date'] >= cut_date].sample(n=30000)