from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDescribeReplicatorRequest(BaseModel):
    ReplicatorArn: StrictStr
