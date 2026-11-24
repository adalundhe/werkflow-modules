from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQDeleteTagsRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
