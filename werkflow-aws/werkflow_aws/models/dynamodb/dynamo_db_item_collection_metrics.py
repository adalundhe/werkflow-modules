from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .dynamo_db_attribute_value import DynamoDBAttributeValue


class DynamoDBItemCollectionMetrics(BaseModel):
    ItemCollectionKey: dict[StrictStr, DynamoDBAttributeValue] | None = None
    SizeEstimateRangeGB: list[StrictFloat | StrictInt] | None = None
