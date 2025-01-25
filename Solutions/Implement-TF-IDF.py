import math
from collections import Counter


def compute_tf_idf(corpus:list[list[str]], query:list[str]):
    """
    Compute TF-IDF scores for a query against a corpus of documents.

    :param corpus: List of documents, where each document is a list of words
    :param query: List of words in the query
    :return: List of lists containing TF-IDF scores for the query words in each document
    """
    
    m, n = len(corpus), len(query)
    
    tf_idf = [[0]*n for _ in range(m)]
    idf = n*[0]
    
    doc_word_counts = [Counter(doc) for doc in corpus]
    doc_lengths = [len(doc) for doc in corpus]
    
    for i, word in enumerate(query):
        doc_count = sum(1 for doc in doc_word_counts if word in doc)
        idf[i] = math.log((m + 1)/(doc_count + 1)) + 1
    

    for i, word in enumerate(query):
        for j in range(m):
            tf_idf[j][i] = round((doc_word_counts[j][word] / doc_lengths[j]) * idf[i], 5)
    
    return tf_idf



corpus = [
    ["the", "cat", "sat", "on", "the", "mat"],
    ["the", "dog", "chased", "the", "cat"],
    ["the", "bird", "flew", "over", "the", "mat"]
]

query = ["cat", "mat"]

print(compute_tf_idf(corpus, query))

