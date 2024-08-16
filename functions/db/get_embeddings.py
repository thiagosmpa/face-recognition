from . import (
    Session,
    Faces,
    json
)
import numpy as np

def get_embeddings(name):
    try:
        with Session() as session:
            user = session.query(Faces).filter(Faces.name == name).first()
            if user:
                embeddings = np.array(json.loads(user.embeddings), dtype=np.float32)
                # embeddings = np.array(eval(embeddings), dtype=np.float32)
                return embeddings
            else:
                return f'No face with name {name} found'

    except Exception as e:
        print(f"\nError getting embedding: {e}\n")