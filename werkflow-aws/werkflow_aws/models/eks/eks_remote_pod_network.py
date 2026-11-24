from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSRemotePodNetwork(BaseModel):
    cidrs: list[StrictStr] | None = None
