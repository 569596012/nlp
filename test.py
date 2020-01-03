from gensim.models import FastText

model_dir = 'D:/PYCHARM/model/'
model_name = 'fasttext.model'
model = FastText.load(model_dir + model_name)

word = '5G'
aa = model.wv.most_similar([word], topn=100)
print(aa)
