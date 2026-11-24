from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DynamoDBBulkOperationBytes(BaseModel):
    BulkPutBytes: StrictInt | None = None
