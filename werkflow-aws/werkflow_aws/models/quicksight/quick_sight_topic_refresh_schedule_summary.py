from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_topic_refresh_schedule import QuickSightTopicRefreshSchedule


class QuickSightTopicRefreshScheduleSummary(BaseModel):
    DatasetId: StrictStr | None = None
    DatasetArn: StrictStr | None = None
    DatasetName: StrictStr | None = None
    RefreshSchedule: QuickSightTopicRefreshSchedule | None = None
