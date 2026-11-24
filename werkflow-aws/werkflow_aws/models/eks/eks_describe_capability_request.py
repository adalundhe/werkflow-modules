from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDescribeCapabilityRequest(BaseModel):
    clusterName: StrictStr
    capabilityName: StrictStr
