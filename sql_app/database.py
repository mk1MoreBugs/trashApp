from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sql_app import settings_db as settings
# create settings_db.py file in sql_app/ with USER_DB, USER_DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME values
SQLALCHEMY_POSTGRES_DB_URL = (
    f"postgresql+psycopg://"
    f"{settings.USER_DB}:{settings.USER_DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)  # postgresql+psycopg://user:password@host:port/dbname[?key=value&key=value...]

engine = create_engine(SQLALCHEMY_POSTGRES_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
