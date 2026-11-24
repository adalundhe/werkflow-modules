from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dynamo_db_bulk_operation_description import DynamoDBBulkOperationDescription


class DynamoDBStartBulkPutItemsResponse(BaseModel):
    BulkOperationDescription: DynamoDBBulkOperationDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
