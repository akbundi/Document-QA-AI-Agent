from rank_bm25 import BM25Okapi
import re

class BM25Retriever:
    def __init__(self, documents):
        self.doc_texts = list(documents.values())
        self.doc_names = list(documents.keys())
        self.tokenized_corpus = [self.tokenize(doc) for doc in self.doc_texts]
        self.bm25 = BM25Okapi(self.tokenized_corpus)

    def tokenize(self, text):
        return re.findall(r'\w+', text.lower())

    def retrieve(self, query, top_k=3):
        tokenized_query = self.tokenize(query)
        scores = self.bm25.get_scores(tokenized_query)
        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
        return [(self.doc_names[i], self.doc_texts[i], scores[i]) for i in top_indices]
