from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQCreateTagsRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: dict[StrictStr, StrictStr] | None = None
