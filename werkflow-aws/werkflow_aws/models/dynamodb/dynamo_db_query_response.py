from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_attribute_value import DynamoDBAttributeValue
from .dynamo_db_consumed_capacity import DynamoDBConsumedCapacity


class DynamoDBQueryResponse(BaseModel):
    Items: list[dict[StrictStr, DynamoDBAttributeValue]] | None = None
    Count: StrictInt | None = None
    ScannedCount: StrictInt | None = None
    LastEvaluatedKey: dict[StrictStr, DynamoDBAttributeValue] | None = None
    ConsumedCapacity: DynamoDBConsumedCapacity | None = None
