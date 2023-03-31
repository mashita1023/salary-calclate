from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URI = (
    f'mariadb://salaryman:pwd@localhost:3306/salaryman'
)

Base = declarative_base()

engine = create_engine(
    DATABASE_URI,
    encoding="utf-8",
    echo=True,
)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()