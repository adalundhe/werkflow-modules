from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDeleteNodegroupRequest(BaseModel):
    clusterName: StrictStr
    nodegroupName: StrictStr
