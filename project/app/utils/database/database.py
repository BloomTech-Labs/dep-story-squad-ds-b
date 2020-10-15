from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# gather environment variables to build the
# connection string for the postgresql database
UN = getenv("RDS_USERNAME")
PW = getenv("RDS_PASSWORD")
HN = getenv("RDS_HOSTNAME")
DBN = getenv("RDS_DB_NAME")

# build out the postgresql login string from environment variables
SQLALCHEMY_DATABASE_URL = f"postgresql://{UN}:{PW}@{HN}/{DBN}"

# create sql engine object
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})

# create sql session object
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create sql base object to be inherited from
Base = declarative_base()


# Dependency for FastAPI
def get_db():
    """Dependency for FastAPI to inject database objects into the path context
    of a request, requires packages `async-exit-stack` and `async-generator`
    to be installed"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
