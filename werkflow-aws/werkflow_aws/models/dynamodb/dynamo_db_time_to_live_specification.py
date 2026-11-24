from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DynamoDBTimeToLiveSpecification(BaseModel):
    Enabled: StrictBool
    AttributeName: StrictStr
