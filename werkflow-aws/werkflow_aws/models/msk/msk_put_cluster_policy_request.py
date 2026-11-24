from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKPutClusterPolicyRequest(BaseModel):
    ClusterArn: StrictStr
    Policy: StrictStr
    CurrentVersion: StrictStr | None = None
