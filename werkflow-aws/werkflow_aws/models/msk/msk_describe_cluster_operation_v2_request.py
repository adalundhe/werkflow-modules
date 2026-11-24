from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDescribeClusterOperationV2Request(BaseModel):
    ClusterOperationArn: StrictStr
