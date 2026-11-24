from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DetectiveStartInvestigationRequest(BaseModel):
    GraphArn: StrictStr
    EntityArn: StrictStr
    ScopeStartTime: datetime.datetime | StrictStr
    ScopeEndTime: datetime.datetime | StrictStr
