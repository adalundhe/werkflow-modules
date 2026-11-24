from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectUpdateResiliencyGroupRequest(BaseModel):
    resiliencyGroupId: StrictStr
    resiliencyGroupName: StrictStr
    clientToken: StrictStr | None = None
