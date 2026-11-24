from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .swf_history_event import SWFHistoryEvent


class SWFGetWorkflowExecutionHistoryResponse(BaseModel):
    events: list[SWFHistoryEvent] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
