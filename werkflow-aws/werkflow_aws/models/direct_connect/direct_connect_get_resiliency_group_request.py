from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectGetResiliencyGroupRequest(BaseModel):
    resiliencyGroupId: StrictStr
