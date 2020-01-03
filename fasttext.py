from gensim.models import FastText

data_dir = 'NewsData/'
file_name = 'cut_words(100~512).txt'

sentences = open(data_dir + file_name, 'r', encoding='utf-8').readlines()
sentences = [sentences[i].strip('\n') for i in range(len(sentences))]
sentences = [sentences[i].split(' ') for i in range(len(sentences))]
sentences = [list(filter(lambda x: len(x) <= 10, sentences[i])) for i in range(len(sentences))]

model = FastText(size=256, window=5, min_count=20, hs=1, sg=1, negative=10, workers=8, sentences=sentences, iter=10)

model.save('model/fasttext.model')

aa
