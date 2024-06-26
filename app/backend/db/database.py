from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://erpjisv1@erpjisv1:Macana11@erpjisv1.mysql.database.azure.com:3306/erpjisv1"

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        