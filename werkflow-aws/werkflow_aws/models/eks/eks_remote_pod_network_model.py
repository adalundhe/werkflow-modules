from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSRemotePodNetworkModel(BaseModel):
    cidrs: list[StrictStr] | None = None
