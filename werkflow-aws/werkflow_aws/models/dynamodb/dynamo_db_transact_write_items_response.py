from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_consumed_capacity import DynamoDBConsumedCapacity
from .dynamo_db_item_collection_metrics import DynamoDBItemCollectionMetrics


class DynamoDBTransactWriteItemsResponse(BaseModel):
    ConsumedCapacity: list[DynamoDBConsumedCapacity] | None = None
    ItemCollectionMetrics: dict[StrictStr, list[DynamoDBItemCollectionMetrics]] | None = None
