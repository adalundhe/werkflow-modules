from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .event_bridge_put_targets_result_entry import EventBridgePutTargetsResultEntry


class EventBridgePutTargetsResponse(BaseModel):
    FailedEntryCount: StrictInt | None = None
    FailedEntries: list[EventBridgePutTargetsResultEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
