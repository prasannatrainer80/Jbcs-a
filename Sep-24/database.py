
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# --------------------------------------------------
# MySQL Database Connection
# --------------------------------------------------

DATABASE_URL = (
    "mysql+pymysql://root:root@localhost:3306/studentdb"
)


# --------------------------------------------------
# Create Engine
# --------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    echo=False
)


# --------------------------------------------------
# Base Class for ORM Models
# --------------------------------------------------

Base = declarative_base()


# --------------------------------------------------
# Session Factory
# --------------------------------------------------

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

