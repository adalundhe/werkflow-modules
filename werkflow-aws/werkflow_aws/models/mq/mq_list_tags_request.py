from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQListTagsRequest(BaseModel):
    ResourceArn: StrictStr
