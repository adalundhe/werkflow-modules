from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDescribeTableReplicaAutoScalingRequest(BaseModel):
    TableName: StrictStr
