from . import (
    Session,
    Faces,
    json
)
import numpy as np

def update_embeddings(name, embeddings):
    try:
        with Session() as session:
            user = session.query(Faces).filter(Faces.name == name).first()
            if user:
                user.embeddings = json.dumps(embeddings.tolist())
                session.commit()
            else:
                return Exception("User not found")

    except Exception as e:
        print(f"\nError getting embedding: {e}\n")