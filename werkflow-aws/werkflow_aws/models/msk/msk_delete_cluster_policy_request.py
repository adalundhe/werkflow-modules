from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDeleteClusterPolicyRequest(BaseModel):
    ClusterArn: StrictStr
