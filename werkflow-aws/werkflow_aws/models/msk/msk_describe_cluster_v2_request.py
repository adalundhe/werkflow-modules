from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDescribeClusterV2Request(BaseModel):
    ClusterArn: StrictStr | None = None
