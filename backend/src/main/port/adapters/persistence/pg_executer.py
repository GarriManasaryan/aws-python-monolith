import logging
from fastapi import HTTPException
from pydantic import BaseModel
from config.app import DbConnector, db_cursor_context
from typing import TypeVar, Type

logger = logging.getLogger(__name__)

T = TypeVar('T', bound=BaseModel)

def select(sql_template: str, cursor: DbConnector, entity: Type[T], values: tuple = ()) -> list[T]:
    cursor.execute(sql_template, values)
    result = cursor.fetchall()
    return [entity(**i) for i in result]


def update(sql_template: str, cursor: DbConnector, values: tuple = ()) -> None:
    try:
        cursor.execute(sql_template, values)
    except Exception as e:
        message = repr(e)
        if 'violates foreign key constraint' in repr(e):
            message = "Foreign key violation"
        raise HTTPException(status_code=404, detail=message)


def get_cursor() -> DbConnector:
    return db_cursor_context.get("db_cursor")


def all_entities(table: str, entity: Type[T]) -> list[T]:
    cursor = get_cursor()
    sql_template = f"select * from {table}"
    return [entity(**i) for i in select(cursor=cursor, sql_template=sql_template)]
