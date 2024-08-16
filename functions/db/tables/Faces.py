from .. import (
    Base,
    Column,
    Integer,
    String
)

class Faces(Base):
    __tablename__ = 'faces'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    embeddings = Column(String, unique=False, nullable=False)