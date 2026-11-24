from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_topic_refresh_details import QuickSightTopicRefreshDetails


class QuickSightDescribeTopicRefreshResponse(BaseModel):
    RefreshDetails: QuickSightTopicRefreshDetails | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
