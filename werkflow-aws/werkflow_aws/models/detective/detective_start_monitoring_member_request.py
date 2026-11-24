from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveStartMonitoringMemberRequest(BaseModel):
    GraphArn: StrictStr
    AccountId: StrictStr
