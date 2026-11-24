from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_scheduled_action import OpenSearchScheduledAction


class OpenSearchListScheduledActionsResponse(BaseModel):
    ScheduledActions: list[OpenSearchScheduledAction] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
