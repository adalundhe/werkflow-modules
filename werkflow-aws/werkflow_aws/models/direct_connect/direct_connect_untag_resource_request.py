from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
