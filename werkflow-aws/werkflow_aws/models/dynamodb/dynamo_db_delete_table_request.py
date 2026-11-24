from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDeleteTableRequest(BaseModel):
    TableName: StrictStr
