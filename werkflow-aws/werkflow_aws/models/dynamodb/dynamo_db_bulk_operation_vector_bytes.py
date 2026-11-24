from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DynamoDBBulkOperationVectorBytes(BaseModel):
    BulkPutVectorBytes: StrictInt | None = None
