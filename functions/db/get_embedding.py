from . import (
    Session,
    Faces,
)
import numpy as np

def get_embedding(name):
    try:
        with Session() as session:
            user = session.query(Faces).filter(Faces.name == name).first()
            if user:
                embedding = user.embeddings
                embedding = np.array(eval(embedding))
            else:
                return None
        
        return embedding

    except Exception as e:
        print(f"\nError getting embedding: {e}\n")