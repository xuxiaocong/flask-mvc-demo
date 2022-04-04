import os
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

from config.settings import SQL_TYPE, SQLITE_URL
from config.settings import POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DATABASE


class DbClient:
    _engine = None
    _base = declarative_base()

    @classmethod
    def get_base(cls):
        return cls._base

    @classmethod
    def get_engine(cls):
        if cls._engine is None:
            if SQL_TYPE == 'SQLITE':
                cls._engine = create_engine(f"sqlite:///{SQLITE_URL}")
            elif SQL_TYPE == 'POSTGRES':
                cls._engine = create_engine(
                    f"postgresql+psycopg2://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"
                )
        return cls._engine

    @classmethod
    def init_table(cls):
        if SQL_TYPE == 'SQLITE':
            cls._base.metadata.create_all(cls.get_engine())
        elif SQL_TYPE == 'POSTGRES':
            init_sql_path = os.path.join('common', 'database', 'init.sql')
            content = ""
            with open(init_sql_path) as f:
                for line in f.readlines():
                    content += line
            sql_list = content.split(';')
            sql_list = sql_list[:-1]

            with cls.get_engine().connect() as conn:
                for sql in sql_list:
                    conn.execute(text(sql))

    @classmethod
    def get_session(cls):
        session = Session(cls.get_engine())
        return session