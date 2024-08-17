from . import (
    Session,
    Faces,
    UniqueViolation,
    json
)
import numpy as np

def create_embeddings(name, embeddings):
    try:
        with Session() as session:
            embeddings = json.dumps(embeddings.tolist())
            user = Faces(name=name, embeddings=embeddings)
            session.add(user)
            session.commit()

    except Exception as e:
        if UniqueViolation:
            print(f"\nFace with name {user.name} already exists\n")