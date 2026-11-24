from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDeleteClusterRequest(BaseModel):
    cluster: StrictStr
