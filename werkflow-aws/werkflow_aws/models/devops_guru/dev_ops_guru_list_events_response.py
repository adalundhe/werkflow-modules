from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_event import DevOpsGuruEvent


class DevOpsGuruListEventsResponse(BaseModel):
    Events: list[DevOpsGuruEvent] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
