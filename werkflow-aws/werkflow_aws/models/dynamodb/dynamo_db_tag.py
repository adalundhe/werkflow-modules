from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBTag(BaseModel):
    Key: StrictStr
    Value: StrictStr
