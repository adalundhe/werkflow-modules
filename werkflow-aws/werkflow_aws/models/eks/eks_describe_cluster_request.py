from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDescribeClusterRequest(BaseModel):
    name: StrictStr
