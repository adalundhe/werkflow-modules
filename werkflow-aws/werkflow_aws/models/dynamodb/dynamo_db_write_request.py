from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_delete_request import DynamoDBDeleteRequest
from .dynamo_db_put_request import DynamoDBPutRequest


class DynamoDBWriteRequest(BaseModel):
    PutRequest: DynamoDBPutRequest | None = None
    DeleteRequest: DynamoDBDeleteRequest | None = None
