import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
class hello:
    def calculate_interest(self,main_array):
            for i in range(len(main_array)):
                main_array[i].sort()
                main_array[i]=' '.join(main_array[i])
            vectorizer = CountVectorizer().fit_transform(main_array)
            vectors = vectorizer.toarray()
            csim = cosine_similarity(vectors)
            def cosine_sim_vectors(vec1, vec2):
                vec1 = vec1.reshape(1,-1)
                vec2 = vec2.reshape(1,-1)
                return cosine_similarity(vec1,vec2)[0][0]
            values=[]
            for i in range(len(vectors)):
                for j in range(len(vectors)):
                    if i==j:
                        continue
                    value=cosine_sim_vectors(vectors[i],vectors[j])
                    values.append(value)
            return sum(values)/len(values)
