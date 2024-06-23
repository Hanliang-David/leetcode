# calculate_tfidf.py
from sklearn.feature_extraction.text import TfidfVectorizer

def calculate_tfidf(corpus):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names_out()
    for doc_index, doc in enumerate(X.toarray()):
        print(f"Document {doc_index + 1}:")
        for term_index, score in enumerate(doc):
            if score > 0:
                print(f"  {feature_names[term_index]}: {score:.4f}")

if __name__ == "__main__":
    documents = [
        "the house had a tiny little mouse",
        "the cat saw the mouse",
        "the mouse ran away from the house",
        "the cat finally ate the mouse",
        "the end of the mouse story"
    ]
    calculate_tfidf(documents)
