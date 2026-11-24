from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteRefreshScheduleRequest(BaseModel):
    DataSetId: StrictStr
    AwsAccountId: StrictStr
    ScheduleId: StrictStr
