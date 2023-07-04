from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(embeddings)

from sklearn.metrics.pairwise import cosine_similarity
aa = ['aaa', 'bbb','ccc']
bb = ['aaa', 'bba','baa']
aaa = model.encode(aa)
bbb = model.encode(bb)
similarities = cosine_similarity(aaa,bbb)
print(similarities)