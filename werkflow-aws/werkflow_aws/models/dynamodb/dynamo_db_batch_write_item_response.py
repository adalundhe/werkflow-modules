from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_consumed_capacity import DynamoDBConsumedCapacity
from .dynamo_db_item_collection_metrics import DynamoDBItemCollectionMetrics
from .dynamo_db_write_request import DynamoDBWriteRequest


class DynamoDBBatchWriteItemResponse(BaseModel):
    UnprocessedItems: dict[StrictStr, list[DynamoDBWriteRequest]] | None = None
    ItemCollectionMetrics: dict[StrictStr, list[DynamoDBItemCollectionMetrics]] | None = None
    ConsumedCapacity: list[DynamoDBConsumedCapacity] | None = None
