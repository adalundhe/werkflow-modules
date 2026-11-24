from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeRefreshScheduleRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSetId: StrictStr
    ScheduleId: StrictStr
