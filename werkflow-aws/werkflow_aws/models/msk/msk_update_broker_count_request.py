from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKUpdateBrokerCountRequest(BaseModel):
    ClusterArn: StrictStr
    CurrentVersion: StrictStr
    TargetNumberOfBrokerNodes: StrictInt
