from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .event_bridge_remove_targets_result_entry import EventBridgeRemoveTargetsResultEntry


class EventBridgeRemoveTargetsResponse(BaseModel):
    FailedEntryCount: StrictInt | None = None
    FailedEntries: list[EventBridgeRemoveTargetsResultEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
