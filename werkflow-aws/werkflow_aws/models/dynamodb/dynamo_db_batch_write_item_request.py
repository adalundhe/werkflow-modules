from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_return_consumed_capacity import DynamoDBReturnConsumedCapacity
from .dynamo_db_return_item_collection_metrics import DynamoDBReturnItemCollectionMetrics
from .dynamo_db_write_request import DynamoDBWriteRequest


class DynamoDBBatchWriteItemRequest(BaseModel):
    RequestItems: dict[StrictStr, list[DynamoDBWriteRequest]]
    ReturnConsumedCapacity: DynamoDBReturnConsumedCapacity | None = None
    ReturnItemCollectionMetrics: DynamoDBReturnItemCollectionMetrics | None = None
