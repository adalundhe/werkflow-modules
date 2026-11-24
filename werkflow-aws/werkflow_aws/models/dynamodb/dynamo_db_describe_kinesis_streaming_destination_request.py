from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDescribeKinesisStreamingDestinationRequest(BaseModel):
    TableName: StrictStr
