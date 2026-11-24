from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_tag import DirectConnectTag


class DirectConnectTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: list[DirectConnectTag]
