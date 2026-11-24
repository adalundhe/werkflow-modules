from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_key_type import DynamoDBKeyType


class DynamoDBKeySchemaElement(BaseModel):
    AttributeName: StrictStr
    KeyType: DynamoDBKeyType
