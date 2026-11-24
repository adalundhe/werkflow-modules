from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_table_description import DynamoDBTableDescription


class DynamoDBDeleteTableResponse(BaseModel):
    TableDescription: DynamoDBTableDescription | None = None
