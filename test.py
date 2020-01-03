from gensim.models import Word2Vec
from gensim import corpora, models
from pprint import pprint
model = models.Word2Vec.load('word2vec.model')


word = '农业'
aa = model.wv.most_similar([word], topn=30)
pprint(aa)
