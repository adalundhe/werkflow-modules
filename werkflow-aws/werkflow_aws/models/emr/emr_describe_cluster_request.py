from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRDescribeClusterRequest(BaseModel):
    ClusterId: StrictStr
