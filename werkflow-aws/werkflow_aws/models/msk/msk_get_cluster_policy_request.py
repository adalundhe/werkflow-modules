from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKGetClusterPolicyRequest(BaseModel):
    ClusterArn: StrictStr
