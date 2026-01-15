import psycopg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

#for dev enviroment:
#from dotenv import load_dotenv
#load_dotenv()

engine = create_engine(os.environ.get("DATABASE_CONECTION_URL", "not avaliable"))
Session = sessionmaker(bind=engine)
Base = declarative_base()


