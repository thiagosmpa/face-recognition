from . import (
    Session,
    Faces,
)
import numpy as np

def get_embeddings(name):
    try:
        with Session() as session:
            user = session.query(Faces).filter(Faces.name == name).first()
            if user:
                embeddings = user.embeddings
                embeddings = np.array(eval(embeddings))
                return embeddings
            else:
                return f'No face with name {name} found'

    except Exception as e:
        print(f"\nError getting embedding: {e}\n")