from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.errors import UniqueViolation

import dotenv
import os
dotenv.load_dotenv()
DB_URL = os.getenv("DB_URL")

engine = create_engine(DB_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

from .Faces import Faces
from .add_face import add_face

Base.metadata.create_all(bind=engine)