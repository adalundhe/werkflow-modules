from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value import DynamoDBAttributeValue
from .dynamo_db_consumed_capacity import DynamoDBConsumedCapacity
from .dynamo_db_item_collection_metrics import DynamoDBItemCollectionMetrics


class DynamoDBPutItemResponse(BaseModel):
    Attributes: dict[StrictStr, DynamoDBAttributeValue] | None = None
    ConsumedCapacity: DynamoDBConsumedCapacity | None = None
    ItemCollectionMetrics: DynamoDBItemCollectionMetrics | None = None
