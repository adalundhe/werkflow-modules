from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_archive import EventBridgeArchive


class EventBridgeListArchivesResponse(BaseModel):
    Archives: list[EventBridgeArchive] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
