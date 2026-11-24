from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_topic_refresh_schedule_summary import QuickSightTopicRefreshScheduleSummary


class QuickSightListTopicRefreshSchedulesResponse(BaseModel):
    TopicId: StrictStr | None = None
    TopicArn: StrictStr | None = None
    RefreshSchedules: list[QuickSightTopicRefreshScheduleSummary] | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
