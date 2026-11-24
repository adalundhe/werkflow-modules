from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_refresh_schedule import QuickSightRefreshSchedule


class QuickSightUpdateRefreshScheduleRequest(BaseModel):
    DataSetId: StrictStr
    AwsAccountId: StrictStr
    Schedule: QuickSightRefreshSchedule
