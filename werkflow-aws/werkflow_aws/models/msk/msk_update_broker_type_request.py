from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MSKUpdateBrokerTypeRequest(BaseModel):
    ClusterArn: StrictStr
    CurrentVersion: StrictStr
    TargetInstanceType: StrictStr
    TopicReassignment: Literal['AUTO', 'MANUAL'] | None = None
