from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDescribeAccessEntryRequest(BaseModel):
    clusterName: StrictStr
    principalArn: StrictStr
