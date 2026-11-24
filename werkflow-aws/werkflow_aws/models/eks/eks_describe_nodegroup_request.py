from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDescribeNodegroupRequest(BaseModel):
    clusterName: StrictStr
    nodegroupName: StrictStr
