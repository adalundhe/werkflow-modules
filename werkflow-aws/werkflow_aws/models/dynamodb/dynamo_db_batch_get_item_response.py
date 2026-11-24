from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value import DynamoDBAttributeValue
from .dynamo_db_consumed_capacity import DynamoDBConsumedCapacity
from .dynamo_db_keys_and_attributes import DynamoDBKeysAndAttributes


class DynamoDBBatchGetItemResponse(BaseModel):
    Responses: dict[StrictStr, list[dict[StrictStr, DynamoDBAttributeValue]]] | None = None
    UnprocessedKeys: dict[StrictStr, DynamoDBKeysAndAttributes] | None = None
    ConsumedCapacity: list[DynamoDBConsumedCapacity] | None = None
