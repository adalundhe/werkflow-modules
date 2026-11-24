from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDeleteGlobalSecondaryIndexAction(BaseModel):
    IndexName: StrictStr
