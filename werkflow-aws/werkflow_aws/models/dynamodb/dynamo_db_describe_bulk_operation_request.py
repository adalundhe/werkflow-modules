from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDescribeBulkOperationRequest(BaseModel):
    BulkOperationArn: StrictStr
