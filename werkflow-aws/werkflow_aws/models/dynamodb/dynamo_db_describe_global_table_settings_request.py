from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDescribeGlobalTableSettingsRequest(BaseModel):
    GlobalTableName: StrictStr
