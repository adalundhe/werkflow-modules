from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDescribeClusterOperationRequest(BaseModel):
    ClusterOperationArn: StrictStr
