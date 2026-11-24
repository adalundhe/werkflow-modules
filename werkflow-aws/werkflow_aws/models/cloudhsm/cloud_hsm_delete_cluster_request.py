from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudHSMDeleteClusterRequest(BaseModel):
    ClusterId: StrictStr
