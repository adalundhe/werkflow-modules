from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_get import DynamoDBGet


class DynamoDBTransactGetItem(BaseModel):
    Get: DynamoDBGet
