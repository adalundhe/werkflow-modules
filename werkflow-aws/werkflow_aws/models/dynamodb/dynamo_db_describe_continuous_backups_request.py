from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDescribeContinuousBackupsRequest(BaseModel):
    TableName: StrictStr
