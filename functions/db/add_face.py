from . import (
    Session,
    Faces,
    UniqueViolation
)
import numpy as np

def add_face(name, embeddings):
    try:
        with Session() as session:
            embeddings = np.array2string(embeddings, separator=',')
            user = Faces(name=name, embeddings='string')
            session.add(user)
            session.commit()

    except Exception as e:
        if UniqueViolation:
            print(f"\nFace with name {user.name} already exists\n")