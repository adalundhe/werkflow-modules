from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_consumed_capacity import DynamoDBConsumedCapacity
from .dynamo_db_item_response import DynamoDBItemResponse


class DynamoDBTransactGetItemsResponse(BaseModel):
    ConsumedCapacity: list[DynamoDBConsumedCapacity] | None = None
    Responses: list[DynamoDBItemResponse] | None = None
