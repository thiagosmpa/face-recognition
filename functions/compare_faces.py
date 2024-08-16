from sklearn.metrics.pairwise import cosine_similarity
from . import extract_features

def compare_faces(img1, img2):
    features1 = extract_features(img1)
    features2 = extract_features(img2)
    if features1 is None or features2 is None:
        return None
    similarity = cosine_similarity(features1, features2)[0][0]
    return similarity