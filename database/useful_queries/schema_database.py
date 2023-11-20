from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.engine.reflection import Inspector

DATABASE_URL = "sqlite:///../test.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
meta = MetaData()

def list_tables_and_schema():
    meta.reflect(bind=engine)
    for table in meta.tables.values():
        print(f"Table: {table.name}")
        for column in table.columns:
            print(f" - Column: {column.name}, Type: {column.type}")


if __name__ == "__main__":
    list_tables_and_schema()
