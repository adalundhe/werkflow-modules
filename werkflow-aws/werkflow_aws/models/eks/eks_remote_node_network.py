from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSRemoteNodeNetwork(BaseModel):
    cidrs: list[StrictStr] | None = None
