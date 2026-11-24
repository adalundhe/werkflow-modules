from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_table_description import DynamoDBTableDescription


class DynamoDBCreateTableResponse(BaseModel):
    TableDescription: DynamoDBTableDescription | None = None
