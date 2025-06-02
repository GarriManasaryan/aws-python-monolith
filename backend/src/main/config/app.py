from contextvars import ContextVar
import os
from typing import Optional

import psycopg2.extras
from dotenv import load_dotenv
from psycopg2._psycopg import cursor
from psycopg2.pool import SimpleConnectionPool

from config.mylogger import logger

load_dotenv()

connection_pool = SimpleConnectionPool(
    2,
    12,
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB_NAME"),
)

DbConnector = cursor
db_cursor_context: ContextVar[Optional[DbConnector]] = ContextVar(
    "db_cursor", default=None
)


class ConnectionFromPool:

    def __init__(self):
        self.connection_pool = None
        self.cursor = None
        self.connection = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor
        )
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)
