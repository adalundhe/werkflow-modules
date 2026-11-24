from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
