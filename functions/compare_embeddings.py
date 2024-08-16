from sklearn.metrics.pairwise import cosine_similarity
from . import extract_features

def compare_embeddings(features1, features2):
    """
        Compare the similarity between two features.
        The similarity is calculated using cosine similarity.
        Use extract_features to get the features before comparing.
    """
    if features1 is None or features2 is None:
        return None
    similarity = cosine_similarity(features1, features2)[0][0]
    return similarity