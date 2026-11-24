from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDescribeGlobalTableRequest(BaseModel):
    GlobalTableName: StrictStr
