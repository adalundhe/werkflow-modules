from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
