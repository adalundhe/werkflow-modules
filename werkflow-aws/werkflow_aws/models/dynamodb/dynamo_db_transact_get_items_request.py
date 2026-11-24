from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_return_consumed_capacity import DynamoDBReturnConsumedCapacity
from .dynamo_db_transact_get_item import DynamoDBTransactGetItem


class DynamoDBTransactGetItemsRequest(BaseModel):
    TransactItems: list[DynamoDBTransactGetItem]
    ReturnConsumedCapacity: DynamoDBReturnConsumedCapacity | None = None
