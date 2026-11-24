from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .direct_connect_tag import DirectConnectTag


class DirectConnectCreateResiliencyGroupRequest(BaseModel):
    resiliencyGroupName: StrictStr
    intendedResiliencyModel: Literal['maximum-resiliency', 'high-resiliency', 'basic-resiliency']
    clientToken: StrictStr | None = None
    tags: list[DirectConnectTag] | None = None
