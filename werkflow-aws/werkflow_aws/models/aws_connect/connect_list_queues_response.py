from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_queue_summary import ConnectQueueSummary


class ConnectListQueuesResponse(BaseModel):
    QueueSummaryList: list[ConnectQueueSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
