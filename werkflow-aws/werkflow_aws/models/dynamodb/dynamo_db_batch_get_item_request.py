from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_keys_and_attributes import DynamoDBKeysAndAttributes
from .dynamo_db_return_consumed_capacity import DynamoDBReturnConsumedCapacity


class DynamoDBBatchGetItemRequest(BaseModel):
    RequestItems: dict[StrictStr, DynamoDBKeysAndAttributes]
    ReturnConsumedCapacity: DynamoDBReturnConsumedCapacity | None = None
