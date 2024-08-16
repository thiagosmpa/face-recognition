from . import (
    Session,
    Faces,
)
import numpy as np

def update_embedding(name, embedding):
    try:
        with Session() as session:
            user = session.query(Faces).filter(Faces.name == name).first()
            if user:
                user.embeddings = str(embedding)
                session.commit()
            else:
                return Exception("User not found")

    except Exception as e:
        print(f"\nError getting embedding: {e}\n")