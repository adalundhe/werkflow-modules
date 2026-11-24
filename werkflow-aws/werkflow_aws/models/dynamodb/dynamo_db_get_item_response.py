from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value import DynamoDBAttributeValue
from .dynamo_db_consumed_capacity import DynamoDBConsumedCapacity


class DynamoDBGetItemResponse(BaseModel):
    Item: dict[StrictStr, DynamoDBAttributeValue] | None = None
    ConsumedCapacity: DynamoDBConsumedCapacity | None = None
