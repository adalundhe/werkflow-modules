from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_topic_refresh_schedule import QuickSightTopicRefreshSchedule


class QuickSightUpdateTopicRefreshScheduleRequest(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
    DatasetId: StrictStr
    RefreshSchedule: QuickSightTopicRefreshSchedule
