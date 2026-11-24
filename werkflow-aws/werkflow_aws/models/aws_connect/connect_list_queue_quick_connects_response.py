from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_quick_connect_summary import ConnectQuickConnectSummary


class ConnectListQueueQuickConnectsResponse(BaseModel):
    NextToken: StrictStr | None = None
    QuickConnectSummaryList: list[ConnectQuickConnectSummary] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
