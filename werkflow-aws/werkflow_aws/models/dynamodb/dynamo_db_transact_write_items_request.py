from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_return_consumed_capacity import DynamoDBReturnConsumedCapacity
from .dynamo_db_return_item_collection_metrics import DynamoDBReturnItemCollectionMetrics
from .dynamo_db_transact_write_item import DynamoDBTransactWriteItem


class DynamoDBTransactWriteItemsRequest(BaseModel):
    TransactItems: list[DynamoDBTransactWriteItem]
    ReturnConsumedCapacity: DynamoDBReturnConsumedCapacity | None = None
    ReturnItemCollectionMetrics: DynamoDBReturnItemCollectionMetrics | None = None
    ClientRequestToken: StrictStr | None = None
