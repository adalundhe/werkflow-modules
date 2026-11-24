from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDeleteClusterRequest(BaseModel):
    name: StrictStr
