from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# build out the postgresql login string from environment variables
SQLALCHEMY_DATABASE_URL = f"postgresql://{getenv("RDS_USERNAME")}:{getenv("RDS_PASSWORD")}@{getenv("RDS_HOSTNAME")}/{getenv("RDS_DB_NAME")}"

# create sql engine object
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})

# create sql session object
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create sql base object to be inherited from
Base = declarative_base()
