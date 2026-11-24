from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDeregisterClusterRequest(BaseModel):
    name: StrictStr
