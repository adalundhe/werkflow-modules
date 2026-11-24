from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDescribeTimeToLiveRequest(BaseModel):
    TableName: StrictStr
