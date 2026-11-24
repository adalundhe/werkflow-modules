from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDescribeClusterRequest(BaseModel):
    ClusterArn: StrictStr | None = None
