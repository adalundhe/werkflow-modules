from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_scheduled_action import OpenSearchScheduledAction


class OpenSearchUpdateScheduledActionResponse(BaseModel):
    ScheduledAction: OpenSearchScheduledAction | None = None
    ResponseMetadata: dict[str, Any] | None = None
