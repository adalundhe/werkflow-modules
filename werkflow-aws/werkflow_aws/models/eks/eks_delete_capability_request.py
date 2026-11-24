from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDeleteCapabilityRequest(BaseModel):
    clusterName: StrictStr
    capabilityName: StrictStr
