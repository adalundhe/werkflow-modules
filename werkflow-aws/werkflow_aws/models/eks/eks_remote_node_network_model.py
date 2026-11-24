from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSRemoteNodeNetworkModel(BaseModel):
    cidrs: list[StrictStr] | None = None
