from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
