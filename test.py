from gensim.models import FastText

model_dir = 'F:/PYCHARM/model/'
model_name = 'fasttext.model'
model = FastText.load(model_dir + model_name)

word = '人工智能'
aa = model.wv.most_similar([word], topn=100)
print(aa)
