from . import (
    Session,
    Faces,
    UniqueViolation
)

def add_face(name, embeddings):
    try:
        with Session() as session:
            user = Faces(name="Thiago", embeddings='string')
            session.add(user)
            session.commit()

    except Exception as e:
        if UniqueViolation:
            print(f"\nFace with name {user.name} already exists\n")